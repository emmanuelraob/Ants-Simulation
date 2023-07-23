from ant import Ant
import pygame

class Colony:
    def __init__(self, size):
        self.size = size
        self.x = 100
        self.y = 100
        self.ants = [Ant(i) for i in range(size)]
        self.food = 1000

    def draw(self, win):
        for ant in self.ants:
            ant.draw(win)
    
    def move_ants(self):
        for ant in self.ants:
            ant.move()

    def eat_once(self):
        for ant in self.ants:
            ant.eat(-3)

    def eat_full(self):
        for ant in self.ants:
            ant.eat(100)

    def view_health(self):
        for ant in self.ants:
            ant.view_health()
    
    def life(self):
        for ant in self.ants:
            ant.life()