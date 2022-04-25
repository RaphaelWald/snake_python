from field import Field
from snake import Snake
import random


class Game:
    def __init__(self, screen):
        self._screen = screen
        self.fields = self.init_fields()
        self.snake = Snake(self)
        self.generate_new_bonus()

    def init_fields(self):
        rows = []
        for i in range(50):
            row = []
            for j in range(50):
                field = Field(self._screen, i*20, j*20)
                row.append(field)
                field.display()
            rows.append(row)
        return rows

    def generate_new_bonus(self):
        x = random.choice(range(50))
        y = random.choice(range(50))
        bonus_field = self.fields[x][y]
        bonus_field.bonus = True
        bonus_field.update((0, 0, 200))
