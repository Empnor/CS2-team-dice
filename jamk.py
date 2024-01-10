def load_players(file_path):
    players = {}
    with open(file_path, 'r') as file:
        for line in file:
            name, price = line.strip().split()
            players[name] = int(price)
    return players

def display_players(players):
    print("Players available for purchase:")
    for name, price in players.items():
        print(f"{name}: ${price}")

def buy_player(players, player_name, buyer_balance):
    if player_name in players:
        player_price = players[player_name]
        if buyer_balance >= player_price:
            print(f"You've successfully bought {player_name} for ${player_price}.")
            buyer_balance -= player_price
            del players[player_name]
        else:
            print("Insufficient funds to buy this player.")
    else:
        print(f"{player_name} is not available for purchase.")

def sell_player(players, player_name, player_price):
    if player_name not in players:
        players[player_name] = player_price
        print(f"You've successfully listed {player_name} for sale at ${player_price}.")
    else:
        print(f"{player_name} is already in the player list.")

def main():
    file_path = 'players.txt'
    player_data = load_players(file_path)

    while True:
        command = input("Enter command (buy/sell/quit): ").lower()

        if command == 'quit':
            break

        if command == 'buy':
            display_players(player_data)
            buyer_balance = int(input("Enter your balance: "))
            player_to_buy = input("Enter the player name you want to buy: ")
            buy_player(player_data, player_to_buy, buyer_balance)

        elif command == 'sell':
            player_to_sell = input("Enter the player name you want to sell: ")
            player_price = int(input("Enter the price for selling the player: "))
            sell_player(player_data, player_to_sell, player_price)

        else:
            print("Invalid command. Please enter 'buy', 'sell', or 'quit'.")

        display_players(player_data)

if __name__ == "__main__":
    main()


