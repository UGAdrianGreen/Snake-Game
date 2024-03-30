import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
snake_speed = 10
snake_x, snake_y = GRID_WIDTH // 2, GRID_HEIGHT // 2
snake_length = 1
snake_body = [(snake_x, snake_y)]
snake_direction = (0, 0)  # (dx, dy)
snake_timer = 0

# Food settings
food_x, food_y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Update snake position
    snake_timer += 1
    if snake_timer >= snake_speed:
        snake_timer = 0
        snake_x += snake_direction[0]
        snake_y += snake_direction[1]

        # Wrap around the screen
        snake_x %= GRID_WIDTH
        snake_y %= GRID_HEIGHT

        # Check for collision with food
        if snake_x == food_x and snake_y == food_y:
            snake_length += 1
            food_x, food_y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

        # Update snake body
        snake_body.insert(0, (snake_x, snake_y))
        if len(snake_body) > snake_length:
            snake_body.pop()

    # Draw snake
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (food_x * GRID_SIZE, food_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Check for collision with snake body
    if (snake_x, snake_y) in snake_body[1:]:
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
