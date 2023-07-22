import pygame

class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, (200, 200, 200), self.rect)
