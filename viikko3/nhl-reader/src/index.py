import requests
from datetime import datetime
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fin_players = list(filter(lambda x: x["nationality"] == "FIN", response))

    players = []

    for fin_player in fin_players:
        player = Player(
            fin_player
        )

        players.append(player)

    print(f"Players from FIN {timestamp}\n")

    for player in sorted(players, key=lambda x: x.goals + x.assists, reverse=True):
        print(player)

if __name__ == "__main__":
    main()