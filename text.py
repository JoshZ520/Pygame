import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)  # For kings

# Initialize the board
board = [
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
]

# Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

# Draw the board
def draw_board(screen):
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 0:  # Light squares
                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Draw pieces
def draw_pieces(screen, board):
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != 0:
                color = RED if piece in [1, 3] else BLUE
                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                radius = SQUARE_SIZE // 3
                pygame.draw.circle(screen, color, center, radius)
                # Draw king marker
                if piece in [3, 4]:
                    pygame.draw.circle(screen, GOLD, center, radius // 2)

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw everything
        draw_board(screen)
        draw_pieces(screen, board)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

# Run the game
main()
