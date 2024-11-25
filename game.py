import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Example")

# Colors
black = (0, 0, 0)
blue = (0, 0, 255)

# Rectangle settings
rect_x, rect_y = 100, 100
rect_width, rect_height = 50, 50
rect_speed = 5

# Clock to control frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed

    # Drawing
    screen.fill(black)  # Clear screen
    pygame.draw.rect(screen, blue, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()  # Update the display

    # Limit frame rate
    clock.tick(60)
