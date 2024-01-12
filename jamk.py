import random


class jamk:
    while True:
        inputti = input("laita komento mitä haluat tehdä ")
        if inputti == "":
            break
        
        if inputti == "arvo tiimi":
            def hae_pelaaja(filename):
                with open(filename, 'r') as file:
                    return [line.strip() for line in file.readlines()]
        igllä = hae_pelaaja('igl.txt')
        bossit = hae_pelaaja('awp.txt')
        entryt = hae_pelaaja('entry.txt')
        lurkit = hae_pelaaja('lurk.txt')
        riflet = hae_pelaaja('rifle.txt')
        
        #onko pelaajia tarpeeksi joka roolissa
        if len(igllä) >= 1 and len(bossit) >= 1 and len(entryt) >= 1 and len(lurkit) >= 1 and len(riflet) >= 1:
            # valitse rooliin pelaaja niin että se ei toista muita pelaajia
            valittu_igl = random.choice(igllä)
            valittu_bossi = random.choice(list(set(bossit) - {valittu_igl}))
            valittu_entry = random.choice(list(set(entryt) - {valittu_igl, valittu_bossi}))
            valittu_lurkki = random.choice(list(set(lurkit) - {valittu_igl, valittu_bossi, valittu_entry}))
            valittu_rifle = random.choice(list(set(riflet) - {valittu_igl, valittu_bossi, valittu_entry, valittu_lurkki}))
        # anna roolit pelaajille
        
        roles = ['IGL', 'AWP', 'Entry', 'Lurk', 'Rifle']
        players_with_roles = {
            valittu_igl: 'IGL',
            valittu_bossi: 'AWP',
            valittu_entry: 'Entry',
            valittu_lurkki: 'Lurk',
            valittu_rifle: 'Rifle'
        }
        for player, role in players_with_roles.items():
            print(f"{player}: {role}")