from ant import Ant
from world_variables import World_Variables
import pygame
import math

world_variables = World_Variables()

class Colony:
    def __init__(self, size):
        self.size = size
        self.ants = {i: Ant(i) for i in range(size)}
        self.food = world_variables.colony_amount_food
        self.deads = 0

    def draw(self, win):
        for ant in self.ants.values():
            ant.draw(win)
    
    def move_ants(self, world_matrix):
        for ant in self.ants.values():
            #look for trace
            ant.verify_direction(world_matrix)
            ant.move(world_matrix,self)
        self.eat_once()

    def eat_once(self):
        for ant in self.ants.values():
            ant.eat(-3)

    def eat_full(self):
        for ant in self.ants.values():
            if self.food > 0:
                ant.eat(1000)
                self.food = 1

    def view_health(self):
        for ant_id, ant in list(self.ants.items()):
            ant.view_health()
            if ant.health <= 0:
                self.remove_ant(ant_id)
    
    def life(self):
        for ant in self.ants.values():
            ant.life()

    
    def add_ant(self):
        new_id = self.size
        self.size += 1
        self.ants[new_id] = Ant(new_id)

    def remove_ant(self, ant_id):
        if ant_id in self.ants:
            del self.ants[ant_id]
            self.size -= 1
            self.deads += 1
    
    def spawn(self):
        if self.food > world_variables.colony_amount_food/2:
            self.add_ant()
            self.food -= 15