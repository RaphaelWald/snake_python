from game import Game
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])
screen.fill((255, 255, 255))
game = Game(screen)

i = 0

# Run until the user asks to quit
running = True
while running:

    if i == 30 and game.snake.moving:
        i = 0
        game.snake.update_deque()
    i = i+1

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and game.snake.direction != "right":
                game.snake.direction = "left"
            elif event.key == pygame.K_RIGHT and game.snake.direction != "left":
                game.snake.direction = "right"
            elif event.key == pygame.K_UP and game.snake.direction != "down":
                game.snake.direction = "up"
            elif event.key == pygame.K_DOWN and game.snake.direction != "up":
                game.snake.direction = "down"

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
