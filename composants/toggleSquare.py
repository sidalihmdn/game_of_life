import pygame

class ToggleSquare:
    """
    A class to represent a toggle square.
    the square can be toggled between black and white
    """
    def __init__(self, x, y, width, color):
        self.rect = pygame.Rect(x, y, width, width)
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def toggle(self):
        if self.color == (0, 0, 0):
            self.color = (255, 255, 255)
        else:
            self.color = (0, 0, 0)