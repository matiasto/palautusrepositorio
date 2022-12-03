class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def tie_score(self, score):
        if score < 3:
            score_lookup = {
                0: "Love",
                1: "Fifteen",
                2: "Thirty"
            }
            return f"{score_lookup[score]}-All"
        else:
            return "Deuce"

    def four_points_or_more(self, score1, score2):
        difference = score1 - score2
        if abs(difference) == 1:
            difference_lookup = {
                1: "Advantage player1",
                -1: "Advantage player2",
            }
            return difference_lookup[difference]
        else:
            return "Win for player1" if difference > 0 else "Win for player2"

    def less_than_four_points(self, score1, score2):
        score_lookup = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return f"{score_lookup[score1]}-{score_lookup[score2]}"

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.tie_score(self.m_score1)
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.four_points_or_more(self.m_score1, self.m_score2)
        else:
            return self.less_than_four_points(self.m_score1, self.m_score2)
