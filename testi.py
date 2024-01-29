import PySimpleGUI as sg
import os
import random
from shutil import copyfile

class Jamk:
    def __init__(self):
        # windowin nimi ja layout       
        self.window = sg.Window('tiimien arvonta', 
                                layout=[[sg.Button('tiimin randomisointi', key='Buttonit'),
                                         sg.Button('IGL', key='uusi_igl'),
                                         sg.Button('AWP', key='uusi_awp'),
                                         sg.Button('ENTRY', key='uusi_entry'),
                                         sg.Button('LURK', key='uusi_lurk'),
                                         sg.Button('RIFLE', key='uusi_rifle'),
                                         sg.Button('Lisää pelaaja', key='lisää_pelaaja')],
                                        [sg.Text('', size=(30, 10), key='roolit')],
                                        [sg.Image(filename='', key='igl_image', size=(50, 50)),
                                         sg.Image(filename='', key='awp_image', size=(50, 50)),
                                         sg.Image(filename='', key='entry_image', size=(50, 50)),
                                         sg.Image(filename='', key='lurk_image', size=(50, 50)),
                                         sg.Image(filename='', key='rifle_image', size=(50, 50))],
                                        [sg.Text("Pelaajan nimi: "), sg.InputText(key='Pelaajan_nimi'),
                                         sg.Text("Rooli: "), sg.Combo(values=['IGL', 'AWP', 'Entry', 'Lurk', 'Rifle'], key='valitse_rooli'),
                                         sg.Text("Kuva pelaajalle: "), sg.InputText(key='image_path'), sg.FileBrowse(key='file_browse')],
                                        ],
                                margins=(50, 50))
        self.roolit = ['IGL', 'AWP', 'Entry', 'Lurk', 'Rifle']
        self.rooli_pelaajat = {}

    # hakee pelaajan
    def hae_pelaaja(self, filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]

    # valitsee rooliin pelaajan
    def valitse_rooli(self):
        igllä = self.hae_pelaaja('igl.txt')
        bossit = self.hae_pelaaja('awp.txt')
        entryt = self.hae_pelaaja('entry.txt')
        lurkit = self.hae_pelaaja('lurk.txt')
        riflet = self.hae_pelaaja('rifle.txt')

        # ettei samoja nimiä valita moneen rooliin
        if len(igllä) >= 1 and len(bossit) >= 1 and len(entryt) >= 1 and len(lurkit) >= 1 and len(riflet) >= 1:
            valittu_igl = random.choice(igllä)
            valittu_bossi = random.choice(list(set(bossit) - {valittu_igl}))
            valittu_entry = random.choice(list(set(entryt) - {valittu_igl, valittu_bossi}))
            valittu_lurkki = random.choice(list(set(lurkit) - {valittu_igl, valittu_bossi, valittu_entry}))
            valittu_rifle = random.choice(
                list(set(riflet) - {valittu_igl, valittu_bossi, valittu_entry, valittu_lurkki}))

            # roolit pelaajiin
            self.rooli_pelaajat = {
                'IGL': valittu_igl,
                'AWP': valittu_bossi,
                'ENTRY': valittu_entry,
                'LURK': valittu_lurkki,
                'RIFLE': valittu_rifle
            }

            # näytä pelaajien kuvat
            for role, player in self.rooli_pelaajat.items():
                image_path = os.path.join('images', f'{player}.png')
                self.window[f'{role.lower()}_image'].update(filename=image_path)

    def näytä_rooli(self):
        roolit_text = ''
        for role, player in self.rooli_pelaajat.items():
            roolit_text += f"{role}: {player}\n"
        self.window['roolit'].update(roolit_text)

    def lisää_pelaaja(self, Pelaajan_nimi, valitse_rooli, image_path):
        if Pelaajan_nimi and valitse_rooli and image_path:
            # kopioi kuva tiedostoon images ja anna sille annetu nimi
            new_image_path = os.path.join('images', f'{Pelaajan_nimi}.png')
            copyfile(image_path, new_image_path)

            # laita pelaajan nimi oikeaan roolin tiedostoon
            with open(f'{valitse_rooli.lower()}.txt', 'a') as file:
                file.write(Pelaajan_nimi + '\n')

    def run(self):
        while True:
            event, values = self.window.read()

            # ikkunan sulkeminen
            if event == sg.WINDOW_CLOSED:
                break

            # buttonit
            if event == 'Buttonit':
                self.valitse_rooli()
                self.näytä_rooli()

            # koko tiimi uusiksi
            elif event == 'uusi_tiimi':
                self.valitse_rooli()
                self.näytä_rooli()

            # yksi rooli uusiksi
            elif event in ['uusi_igl', 'uusi_awp', 'uusi_entry', 'uusi_lurk', 'uusi_rifle']:
                role = event.split('_')[1].upper()
                self.rooli_pelaajat[role] = random.choice(self.hae_pelaaja(f'{role.lower()}.txt'))
                self.window[f'{role.lower()}_image'].update(filename=os.path.join('images', f'{self.rooli_pelaajat[role]}.png'))
                self.näytä_rooli()

            # lisää pelaaja
            elif event == 'lisää_pelaaja':
                Pelaajan_nimi = values['Pelaajan_nimi']
                valitse_rooli = values['valitse_rooli']
                image_path = values['image_path'] if 'image_path' in values else None

                if Pelaajan_nimi and valitse_rooli and image_path:
                    self.lisää_pelaaja(Pelaajan_nimi, valitse_rooli, image_path)
                    sg.popup(f'Pelaaja {Pelaajan_nimi} lisätty rooliin {valitse_rooli}.')

        self.window.close()

if __name__ == "__main__":
    app = Jamk()
    app.run()
