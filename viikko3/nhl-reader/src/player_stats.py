class PlayerStats:
    def __init__(self, reader):
        self.__reader = reader

    def top_scorers_by_nationality(self, nationality):
        return sorted(
            filter(lambda x: x.nationality ==
                   nationality, self.__reader.players),
            key=lambda x: x.points,
            reverse=True
        )
