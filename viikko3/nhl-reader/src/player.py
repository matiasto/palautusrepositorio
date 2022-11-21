class Player:
    def __init__(self, player_dict):
        self.__name = player_dict["name"]
        self.__nationality = player_dict["nationality"]
        self.__assists = player_dict["assists"]
        self.__goals = player_dict["goals"]
        self.__penalties = player_dict["penalties"]
        self.__team = player_dict["team"]
        self.__games = player_dict["games"]
        self.__points = player_dict["assists"] + player_dict["goals"]

    def __str__(self) -> str:
        return f"{self.__name:<20} {self.__team:3} {self.__games:2} + {self.__assists:2} = {self.__points:2}"

    @property
    def name(self):
        return self.__name

    @property
    def nationality(self):
        return self.__nationality

    @property
    def assists(self):
        return self.__assists

    @property
    def goals(self):
        return self.__goals

    @property
    def penalties(self):
        return self.__penalties

    @property
    def team(self):
        return self.__team

    @property
    def games(self):
        return self.__games

    @property
    def points(self):
        return self.__points
