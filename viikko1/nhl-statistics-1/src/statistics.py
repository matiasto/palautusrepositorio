


class Statistics:
    def __init__(self, player_reader: object):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=None):
        sort_key = lambda player: player.points
        if not sort_by:
            pass
        elif not callable(sort_by):
            raise TypeError("invalid sort_by value")
        else:
            sort_key = sort_by

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_key
        )

        result = []
        i = 1
        while i <= how_many:
            result.append(sorted_players[i-1])
            i += 1

        return result
