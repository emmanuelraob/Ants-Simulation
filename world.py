import pygame
from world_variables import World_Variables
from obstacle import Obstacle

world_variables = World_Variables()

class World:
    
    def __init__(self):
        white_color = world_variables.background_color
        self.world_matrix = [[white_color for _ in range(world_variables.screenX//4)]for _ in range(world_variables.screenY//4)]
        self.obstacles = Obstacle(200,200,10,10)
    
    def draw(self, win):
        for y in range(world_variables.screenY//4):
            for x in range(world_variables.screenX//4):
                r, g, b = self.world_matrix[y][x]
                if r>0+world_variables.gradient:
                    r-=world_variables.gradient
                if g>0+world_variables.gradient:
                    g-=world_variables.gradient
                if b>0+world_variables.gradient:
                    b-=world_variables.gradient
                self.world_matrix[y][x] = (r, g, b)
                pygame.draw.rect(win, self.world_matrix[y][x], pygame.Rect(x*4, y*4, 4, 4))
        self.obstacles.draw(win)
        

