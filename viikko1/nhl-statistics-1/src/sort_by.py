from enum import Enum


class SortBy(Enum):
    POINTS = lambda player: player.points
    GOALS = lambda player: player.goals
    ASSISTS = lambda player: player.assists