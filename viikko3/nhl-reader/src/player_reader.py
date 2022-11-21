import requests
from datetime import datetime
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.__url = url
        self.__timestamp = None
        self.__players = self.__get_players()

    @property
    def players(self):
        return self.__players

    @property
    def timestamp(self):
        return self.__timestamp

    def __get_players(self):
        response = requests.get(self.__url).json()
        self.__timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return [Player(player) for player in response]
