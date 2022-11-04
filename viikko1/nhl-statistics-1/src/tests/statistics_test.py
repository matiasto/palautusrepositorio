import unittest
from statistics import Statistics
from player import Player
from sort_by import SortBy


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_instantiation(self):
        self.assertEqual(5, len(self.statistics._players))

    def test_search(self):
        player = self.statistics.search("Kurri")
        self.assertEqual("Kurri", player.name)

    def test_search_returns_none_if_player_not_found(self):
        player = self.statistics.search("Kurriii")
        self.assertEqual(None, player)

    def test_team(self):
        players = self.statistics.team("EDM")
        self.assertEqual(3, len(players))

    def test_top(self):
        players = self.statistics.top(2)
        self.assertEqual(2, len(players))
        self.assertEqual("Gretzky", players[0].name)
        self.assertEqual("Lemieux", players[1].name)

    def test_top_with_sort_by_goals(self):
        players = self.statistics.top(2, SortBy.GOALS)
        self.assertEqual(2, len(players))
        self.assertEqual("Lemieux", players[0].name)
        self.assertEqual("Yzerman", players[1].name)

    def test_top_with_sort_by_assists(self):
        players = self.statistics.top(2, SortBy.ASSISTS)
        self.assertEqual(2, len(players))
        self.assertEqual("Gretzky", players[0].name)
        self.assertEqual("Yzerman", players[1].name)

    def test_top_with_sort_by_points(self):
        players = self.statistics.top(2, SortBy.POINTS)
        self.assertEqual(2, len(players))
        self.assertEqual("Gretzky", players[0].name)
        self.assertEqual("Lemieux", players[1].name)

    def test_top_with_sort_by_raises_value_error_if_unknown_sort_by(self):
        with self.assertRaises(TypeError):
            self.statistics.top(2, "unknown")
    