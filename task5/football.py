from results import Results

class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
        return f'Футбольных побед: {self.victories}'

    def number_of_draws(self):
        return f'Футбольных ничьих: {self.draws}'

    def number_of_losses(self):
        return f'Футбольных поражений: {self.losses}'

    def total_points(self):
        total_points = 3 * self.victories + self.draws
        return f'Общее количество очков: {total_points}'
