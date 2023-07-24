import pygame
import random

WIN_WIDTH, WIN_HEIGHT = 800, 600
FOOD_RADIUS = 5

class Food:
    def __init__(self):
        self.food_left = 100
        self.x = 100
        self.y = 100
        self.color = (0,255,0)

    def draw(self, win):
        food = self.food_left
        food = self.map_range(food,0,100,1,7)
        pygame.draw.circle(win, self.color, (self.x, self.y), food)

    def map_range(self, value, x1, x2, y1, y2):
        return y1 + (value - x1) * (y2 - y1) / (x2 - x1)

    
    def move(self, posx, posy):
            self.x = posx
            self.y = posy