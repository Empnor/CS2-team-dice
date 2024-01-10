saldo = 2000

class Jamk:
    def __init__(self):
        pass  # You can add any initialization code here if needed

    def main_loop(self):
        while True:
            lol = input("Kirjoita komento. Jos haluat lopettaa pelin, jätä tyhjäksi. Jos haluat tietää komennot, kirjoita 'komennot': ")
            if lol == "":
                break
            elif lol == "pelaaja lista":
                self.buy_players()

    def buy_players(self):
        # Add code here to read players from players.txt and implement buying logic
        print("Ostetaan pelaajia!")

# Instantiate the Jamk class and run the main loop
game_instance = Jamk()
game_instance.main_loop()
