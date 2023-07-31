import random
from obstacle import Obstacle

from world_variables import World_Variables
world_variables = World_Variables()

class Obstacles:
    def __init__(self):
        self.obstacles = [Obstacle(random.uniform(10,world_variables.screenX),random.uniform(10,world_variables.screenY),10,10) for i in range(100)]
        self.obstacles.append(Obstacle(-5,-5,5,world_variables.screenY+10)) #left wall
        self.obstacles.append(Obstacle(world_variables.screenX,-5,5,world_variables.screenY+10)) #rigth wall
        self.obstacles.append(Obstacle(-5,-5,world_variables.screenX+10,5)) #uper wall
        self.obstacles.append(Obstacle(-5,world_variables.screenY,world_variables.screenX+10,5)) #down wall



    def draw(self,win):    
        for obstacle in self.obstacles:
            obstacle.draw(win)

    def verify_pos(self,x,y):
        for obstacle in self.obstacles:
            if obstacle.crash(x,y):
                return True
        return False
