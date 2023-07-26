import pygame
from world_variables import World_Variables
world_variables = World_Variables()

class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, world_variables.obstacle_color, self.rect)
