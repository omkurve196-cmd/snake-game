import pygame
import random

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Snake function
def draw_snake(size, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, size, size])

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH/6, HEIGHT/3])

def game():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2

    snake_list = []
    snake_length = 1

    snake_size = 15
    dx = 0
    dy = 0

    food_x = round(random.randrange(0, WIDTH - snake_size) / 15) * 15
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 15) * 15

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C-Play Again or Q-Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_size
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_size
                    dx = 0

        x += dx
        y += dy

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size])

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Colliding with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_size, snake_list)
        pygame.display.update()

        # Eating food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_size) / 15) * 15
            food_y = round(random.randrange(0, HEIGHT - snake_size) / 15) * 15
            snake_length += 1

        clock.tick(10)

    pygame.quit()
    quit()

game()
