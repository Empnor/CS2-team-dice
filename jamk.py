import PySimpleGUI as sg
import os
import random

class Jamk:
    def __init__(self):
                # windowin nimi ja layout
        self.window = sg.Window('tiimien arvonta', 
                                layout=[[sg.Button('tiimin randomisointi', key='Buttonit'),
                                         sg.Button('IGL', key='uusi_igl'),
                                         sg.Button('AWP', key='uusi_awp'),
                                         sg.Button('ENTRY', key='uusi_entry'),
                                         sg.Button('LURK', key='uusi_lurk'),
                                         sg.Button('RIFLE', key='uusi_rifle')],
                                        [sg.Text('', size=(30, 10), key='roolit')],
                                        [sg.Image(filename='', key='igl_image', size=(50, 50)),
                                         sg.Image(filename='', key='awp_image', size=(50, 50)),
                                         sg.Image(filename='', key='entry_image', size=(50, 50)),
                                         sg.Image(filename='', key='lurk_image', size=(50, 50)),
                                         sg.Image(filename='', key='rifle_image', size=(50, 50))],
                                            [sg.Text("uusi kuva pelaajalle: "), sg.FileBrowse()]],
                                margins=(50, 50))
        #roolit kerrotaan
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

            # roolit
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

    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Buttonit':
                self.valitse_rooli()
                self.näytä_rooli()

            # koko tiimi uusiksi
            elif event == 'uusi_tiimi':
                self.valitse_rooli()
                self.näytä_rooli()

            #yksi rooli uusiksi
            elif event in ['uusi_igl', 'uusi_awp', 'uusi_entry', 'uusi_lurk', 'uusi_rifle']:
                role = event.split('_')[1].upper()
                self.rooli_pelaajat[role] = random.choice(self.hae_pelaaja(f'{role.lower()}.txt'))
                self.window[f'{role.lower()}_image'].update(filename=os.path.join('images', f'{self.rooli_pelaajat[role]}.png'))
                self.näytä_rooli()

        self.window.close()


if __name__ == "__main__":
    app = Jamk()
    app.run()