from composants.squareGrid import SquareGrid
import pygame

#parameters
COL : int = 70
ROW : int = 70


# Initialize Pygame
pygame.init()

# Set up display
window_size = (ROW*12, COL*12)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid of Toggle Squares")

# Create a grid of 5 rows and 8 columns with square size of 50
grid = SquareGrid(
    rows=ROW,
    cols=COL,
    squareSize=10,
    spacing=2)  # 5 rows, 8 columns, square size 50, with 10 px spacing

# Set up clock for frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
playing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click to toggle square color
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # Get the position of the mouse click
            grid.handle_click(pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing

    # Fill the window with a background color
    window.fill((128, 128, 128))
    # Draw the grid of squares

    grid.draw(window)

    if playing:
        grid.update()

    # Update the display
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)

# Quit Pygame
pygame.quit()
