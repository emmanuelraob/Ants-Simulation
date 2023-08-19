import pygame
from obstacles.obstacle import Obstacle
from world.world_variables import World_Variables
world_variables = World_Variables()


class Meal(Obstacle):
    def __init__(self, x, y, r):
        self.r = r
        super().__init__(x, y, 2*r, 2*r)

    def draw(self, win):
        pygame.draw.rect(win, world_variables.food_color, self.rect, border_radius=self.r)
