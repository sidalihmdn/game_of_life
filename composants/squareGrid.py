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
                row_squares.append(ToggleSquare(x, y, self.square_size, (0, 255, 0)))
            self.squares.append(row_squares)

    def draw(self, window):
        # Draw all squares in the grid
        for row_squares in self.squares:
            for square in row_squares:
                square.draw(window)