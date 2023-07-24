import pygame
from world_variables import World_Variables

world = World_Variables()

class World:
    
    def __init__(self):
        white_color = (255,255,255)
        self.world_matrix = [[white_color for _ in range(world.screenX//4)]for _ in range(world.screenY//4)]
    
    def draw(self, win):
        for y in range(world.screenY//4):
            for x in range(world.screenX//4):
                r, g, b = self.world_matrix[y][x]
                gradient = 2
                if r<255-gradient:
                    r+=gradient
                if g<255-gradient:
                    g+=gradient
                if b<255-gradient:
                    b+=gradient
                self.world_matrix[y][x] = (r, g, b)
                pygame.draw.rect(win, self.world_matrix[y][x], pygame.Rect(x*4, y*4, 4, 4))

