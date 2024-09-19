import pygame
from composants.toggleSquare import ToggleSquare

class SquareGrid:
    def __init__(self, rows, cols, squareSize=50, spacing=5):
        self.rows = rows
        self.cols = cols
        self.square_size = squareSize
        self.spacing = spacing  # Optional: spacing between squares
        self.squares = []  # List to hold all the squares in the grid

        # Create the grid of squares
        for row in range(self.rows):
            row_squares = []
            for col in range(self.cols):
                x = col * (self.square_size + self.spacing)
                y = row * (self.square_size + self.spacing)
                row_squares.append(ToggleSquare(x, y, self.square_size, (0, 0, 0)))
            self.squares.append(row_squares)

    def draw(self, window):
        # Draw all squares in the grid
        for row_squares in self.squares:
            for square in row_squares:
                square.draw(window)

    def handle_click(self, pos):
        # Check if the mouse click is within the grid
        if pos[0] < self.cols * (self.square_size + self.spacing) and pos[1] < self.rows * (self.square_size + self.spacing):
            # Calculate the row and column of the square clicked
            col = pos[0] // (self.square_size + self.spacing)
            row = pos[1] // (self.square_size + self.spacing)
            # Toggle the color of the square
            self.squares[row][col].toggle()

    def update(self):
        # impelement the life game logic
        for i in range(self.rows):
            for j in range(self.cols):
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        if 0 <= i + x < self.rows and 0 <= j + y < self.cols:
                            count += self.squares[i + x][j + y].color == pygame.Color('white')
                if self.squares[i][j].color == pygame.Color('white'):
                    if count < 2 or count > 3:
                        self.squares[i][j].toggle()
                elif count == 3:
                    self.squares[i][j].toggle()
        
        pygame.time.wait(100)
        