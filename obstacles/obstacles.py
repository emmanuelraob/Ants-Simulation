import random
from obstacles.obstacle import Obstacle
from QuadTree.quadTree import QuadTree

from world_variables import World_Variables
world_variables = World_Variables()

class Obstacles:
    def __init__(self):
        self.obstacles = [Obstacle(random.uniform(10,world_variables.screenX),random.uniform(10,world_variables.screenY),10,10) for i in range(world_variables.obstacle_amount)]
        self.obstacles.append(Obstacle(-5,-5,5,world_variables.screenY+10)) #left wall
        self.obstacles.append(Obstacle(world_variables.screenX,-5,5,world_variables.screenY+10)) #rigth wall
        self.obstacles.append(Obstacle(-5,-5,world_variables.screenX+10,5)) #uper wall
        self.obstacles.append(Obstacle(-5,world_variables.screenY,world_variables.screenX+10,5)) #buttom wall

        self.tree = QuadTree( world_variables.tree_depth, -5, -5, world_variables.screenX+10, world_variables.screenY+15, objects=self.obstacles)

    def draw(self,win):    
        for obstacle in self.obstacles:
            obstacle.draw(win)

    def verify_pos(self,x,y):
        list =  self.tree.get_in_region(x,y)
        if not list == None:
            for obstacle in list:
                if obstacle.crash(x,y):
                    return True
        return False
