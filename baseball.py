class Baseball:
    def __init__(self, name, games, win, lose, draw):
        self.name = name
        self.games = games
        self.win = win
        self.lose = lose
        self.draw = draw

    def win_rate(self):
        return self.win / (self.win + self.lose)

    def game_behind_c(self):
        return (21 - (self.win - self.lose)) / 2

    def game_behind_p(self):
        return (15 - (self.win - self.lose)) / 2

    def team_grades_c(self):
        print(
            f'{self.name:12s},{self.games:4d},{self.win:3d},{self.lose:3d},{self.draw:3d},{self.win_rate():.3f},{self.game_behind_c():.1f}')

    def team_grades_p(self):
        print(
            f'{self.name:12s},{self.games:4d},{self.win:3d},{self.lose:3d},{self.draw:3d},{self.win_rate():.3f},{self.game_behind_p():.1f}')
