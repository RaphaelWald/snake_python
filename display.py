import pygame


class Display:
    def __init__(self, screen, x, y, x_length, y_length):
        self.screen = screen
        self.x = x
        self.y = y
        self.x_length = x_length
        self.y_length = y_length
        self.font = pygame.font.SysFont('ligconsolata', 50)

    def display(self, content):
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
            self.x, self.y, self.x_length, self.y_length))
        text = self.font.render(
            content, True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.x + self.x_length/2,
                           self.y + self.y_length/2)
        self.screen.blit(text, textRect)
