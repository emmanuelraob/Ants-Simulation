from ant import Ant
import pygame

class Colony:
    def __init__(self, size):
        self.size = size
        self.x = 100
        self.y = 100
        self.ants = {i: Ant(i) for i in range(size)}
        self.food = 1000

    def draw(self, win):
        for ant in self.ants.values():
            ant.draw(win)
    
    def move_ants(self):
        for ant in self.ants.values():
            ant.move()

    def eat_once(self):
        for ant in self.ants.values():
            ant.eat(-3)

    def eat_full(self):
        for ant in self.ants.values():
            ant.eat(1000)

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
