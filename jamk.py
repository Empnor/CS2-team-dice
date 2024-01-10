import random


class jamk:
    while True:
        lol = input("laita komento mitä haluat tehdä")
        if lol == "":
            break
        
        if lol == "arvo":
            def hae_pelaaja(filename):
                with open(filename, 'r') as file:
                    return [line.strip() for line in file.readlines()]
        igllä = hae_pelaaja('igl.txt')
        bossit = hae_pelaaja('awp.txt')
        entryt = hae_pelaaja('entry.txt')
        lurk_players = hae_pelaaja('lurk.txt')
        rifle_players = hae_pelaaja('rifle.txt')
        #onko pelaajia tarpeeksi joka roolissa
        if len(igllä) >= 1 and len(bossit) >= 1 and len(entryt) >= 1 and len(lurk_players) >= 1 and len(rifle_players) >= 1:
            # valitse rooliin pelaaja niin että se ei toista muita pelaajia
            selected_igl = random.choice(igllä)
            selected_awp = random.choice(list(set(bossit) - {selected_igl}))
            selected_entry = random.choice(list(set(entryt) - {selected_igl, selected_awp}))
            selected_lurk = random.choice(list(set(lurk_players) - {selected_igl, selected_awp, selected_entry}))
            selected_rifle = random.choice(list(set(rifle_players) - {selected_igl, selected_awp, selected_entry, selected_lurk}))
        # anna roolit pelaajille
        roles = ['IGL', 'AWP', 'Entry', 'Lurk', 'Rifle']
        players_with_roles = {
            selected_igl: 'IGL',
            selected_awp: 'AWP',
            selected_entry: 'Entry',
            selected_lurk: 'Lurk',
            selected_rifle: 'Rifle'
        }
        for player, role in players_with_roles.items():
            print(f"{player}: {role}")
   


