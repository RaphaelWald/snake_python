import pygame
from field import Field
from snake import Snake
from display import Display
import random

START_DURATION = 100_000_000


class Game:
    def __init__(self, screen):
        self._screen = screen
        self.fields = self.init_fields()
        self.snake = Snake(self)
        self.duration = START_DURATION
        self.duration_factor = 0.9999
        self.length_display = Display(screen, 100, 1000, 300, 80)
        self.velocity_display = Display(screen, 600, 1000, 300, 80)
        self.generate_new_bonus()

    def update_duration(self):
        self.duration *= self.duration_factor

    @property
    def velocity(self):
        return 1 / (self.duration / START_DURATION)

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

    def display_stats(self):
        pygame.draw.rect(self._screen, (0, 0, 0),
                         pygame.Rect(0, 1000, 1000, 100))
        self.length_display.display(f"Score: {len(self.snake)}")
        self.velocity_display.display(f"Speed: {round(self.velocity, 2)}")
