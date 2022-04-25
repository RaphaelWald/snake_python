from game import Game
import time
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1080])
screen.fill((255, 255, 255))
game = Game(screen)

i = 0
temp = "right"
duration = 100_000_000
# Run until the user asks to quit
running = True
last = time.perf_counter_ns()
while running:
    current = time.perf_counter_ns()
    if game.snake.moving and current - last > game.duration:
        game.snake.direction = temp
        game.snake.update_deque()
        last = current
        game.update_duration()
        game.display_stats()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and game.snake.direction != "right":
                temp = "left"
            elif event.key == pygame.K_RIGHT and game.snake.direction != "left":
                temp = "right"
            elif event.key == pygame.K_UP and game.snake.direction != "down":
                temp = "up"
            elif event.key == pygame.K_DOWN and game.snake.direction != "up":
                temp = "down"

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
