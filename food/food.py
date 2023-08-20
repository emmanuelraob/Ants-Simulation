import pygame
import random
import math
from food.meal import Meal
from QuadTree.quadTree import QuadTree
from world.world_variables import World_Variables
world_variables = World_Variables()


class Food:
    def __init__(self):
        self.meals = []
        self.build()
        self.tree = QuadTree( world_variables.tree_depth, -5, -5, world_variables.screenX+10, world_variables.screenY+15, objects=self.meals)
        
    def draw(self, win):
        for meal in self.meals:
            meal.draw(win)
    
    def build(self):
        for j in range(world_variables.food_collection_amount):
            x_center = random.uniform(world_variables.food_collection_radius, world_variables.screenX-world_variables.food_collection_radius)
            y_center = random.uniform(world_variables.food_collection_radius, world_variables.screenY-world_variables.food_collection_radius)
            
            for i in range(world_variables.food_amount_collection):
                angle = random.uniform(0, 2 * math.pi) 
                r = world_variables.food_collection_radius * math.sqrt(random.uniform(0, 1)) 
                
                x = x_center + r * math.cos(angle)
                y = y_center + r * math.sin(angle)

                self.meals.append(Meal(x, y, 1))
    
    def verify_pos(self, x, y):
        list = self.tree.get_in_region(x,y)
        if not list == None:
            for meal in list:
                if meal.crash(x,y):
                    return meal
        return False