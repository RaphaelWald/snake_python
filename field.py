import pygame


class Field:
    def __init__(self, screen, x, y):
        self._screen = screen
        self.x = x
        self.y = y
        self.size = 20
        self.border_size = 1
        self.color = (255, 255, 255)
        self.bonus = False

    def display(self):
        pygame.draw.rect(self._screen, (230, 230, 230), pygame.Rect(
            self.x, self.y, self.size, self.size))
        pygame.draw.rect(self._screen, self.color, pygame.Rect(
            self.x + self.border_size, self.y + self.border_size, self.size -
            2*self.border_size, self.size - 2*self.border_size))

    def update(self, color):
        self.color = color
        self.display()
