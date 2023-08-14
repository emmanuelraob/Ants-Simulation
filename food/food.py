import pygame
import random

from world.world_variables import World_Variables
world_variables = World_Variables()

class Food:
    def __init__(self, x, y):
        self.circle = pygame.
        self.food_left = 100
        self.x = x
        self.y = y

    def draw(self, win):
        food = self.food_left
        food = self.map_range(food,0,100,1,7)
        pygame.draw.circle(win, self.color, (self.x, self.y), food)

    def map_range(self, value, x1, x2, y1, y2):
        return y1 + (value - x1) * (y2 - y1) / (x2 - x1)

    
    def move(self, posx, posy):
            self.x = posx
            self.y = posy