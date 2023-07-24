import pygame
from world_variables import World_Variables

world = World_Variables()

class World:
    
    def __init__(self):
        white_color = [0,0,0]
        world_matrix = [[white_color for _ in range(world.screenX)]for _ in range(world.screenY)]
    
    def draw(self, win):
        for y in range(world.screenY):
            for x in range(world.screenX):
                pygame.draw.rect(win, self.world_matrix[y][x], pygame.Rect(x, y, 1, 1))
        pass