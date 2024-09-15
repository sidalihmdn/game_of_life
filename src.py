from composants.squareGrid import SquareGrid
import pygame

# Initialize Pygame
pygame.init()

# Set up display
window_size = (600, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid of Toggle Squares")

# Create a grid of 5 rows and 8 columns with square size of 50
grid = SquareGrid(
    rows=5,
    cols=8,
    squareSize=50,
    spacing=10)  # 5 rows, 8 columns, square size 50, with 10 px spacing

# Set up clock for frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click to toggle square color
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # Get the position of the mouse click
            grid.handle_click(pos)

    # Fill the window with a background color
    window.fill((128, 128, 128))

    # Draw the grid of squares
    grid.draw(window)

    # Update the display
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)

# Quit Pygame
pygame.quit()
