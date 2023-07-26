import random
from obstacle import Obstacle

from world_variables import World_Variables
world_variables = World_Variables()

class Obstacles:
    def __init__(self):
        self.obstacles = [Obstacle(random.uniform(10,world_variables.screenX),random.uniform(10,world_variables.screenY),10,10) for i in range(100)]
        

    def draw(self,win):    
        for obstacle in self.obstacles:
            obstacle.draw(win)

    def verify_pos(self,x,y):
        for obstacle in self.obstacles:
            if obstacle.crash(x,y):
                return True
        return False
