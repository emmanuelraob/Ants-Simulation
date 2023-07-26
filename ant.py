import random
import math
import random
import pygame
from enum import Enum
from world_variables import World_Variables
from world import World

world_variables = World_Variables()
WIN_WIDTH, WIN_HEIGHT = world_variables.screenX, world_variables.screenY
HEALTH, FOOD = 30*10,30*120 #30*30, 30*120 #30*30, #30*120
ANT_RADIUS = 2

class State (Enum):
    LOOKING_FOR_FOOD = 1
    COMING_BACK_COLONY = 2
    WAITING = 3
    CARRYING_FOOD = 4 


class Ant:
    def __init__(self, id, x=WIN_WIDTH/2 , y=WIN_HEIGHT/2 ):
        self.id = id
        self.x = x
        self.y = y
        self.health = HEALTH  # this amount of heath last for 30 seconds before the ant die
        self.food = FOOD # this amount of food last arround 2 minutes
        self.speed = random.uniform(0.5,1.5)
        self.angle = random.uniform(0, 2*math.pi)  # ants start with a random orientation
        self.color = world_variables.ant_color
        self.distance = 0
        self.next_distance = random.uniform(10,30) # to move in little lines
        self.state = State.LOOKING_FOR_FOOD
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), ANT_RADIUS)

    def look_for_food(self,world_matrix):
        if self.distance < self.next_distance :
            self.x = self.x + self.speed * math.cos(self.angle)
            self.y = self.y + self.speed * math.sin(self.angle)
            self.distance += self.speed
        
        elif self.distance >= self.next_distance:
            self.distance = 0
            self.next_distance = random.uniform(10,30)
            self.angle = self.angle + random.uniform(-2,2)
            self.state = State.WAITING

        # If the ant hits the left or right edge of the screen, adjust its angle by π plus a random amount
        if self.x < ANT_RADIUS or self.x > WIN_WIDTH - ANT_RADIUS:
            self.angle = math.pi - self.angle + random.uniform(-0.5, -0.5)

        # If the ant hits the top or bottom edge of the screen, flip the sign of its angle and add a random amount
        if self.y < ANT_RADIUS or self.y > WIN_HEIGHT - ANT_RADIUS:
            self.angle = -self.angle + random.uniform(-0.5, 0.5)

    def go_to_colony(self,world_matrix):
        dx = (WIN_WIDTH // 2) - self.x
        dy = (WIN_HEIGHT // 2) - self.y
        if math.sqrt(dx**2 + dy**2) > 3:
            self.angle = math.atan2((WIN_HEIGHT // 2) - self.y, (WIN_WIDTH // 2) - self.x)
            self.x = self.x + self.speed * math.cos(self.angle)
            self.y = self.y + self.speed * math.sin(self.angle)
            #if self.x>=0 and self.y>=0 and self.x<=WIN_WIDTH and self.y<=WIN_HEIGHT:
                #world_matrix.world_matrix[int(self.y/4)][int(self.x/4)] = world_variables.ant_trace_back
        else:
            self.in_colony()

        

    def in_colony(self):
        self.color = world_variables.ant_color
        self.food = FOOD
        self.state = State.LOOKING_FOR_FOOD
    
    def carry_food(self):
        self.go_to_colony()

    def wait(self):
        self.state = State.LOOKING_FOR_FOOD

    def move(self, world_matrix):
        if self.state == State.LOOKING_FOR_FOOD:
            self.look_for_food(world_matrix)
        elif self.state == State.COMING_BACK_COLONY:
            self.go_to_colony(world_matrix)
        elif self.state == State.CARRYING_FOOD:
            self.carry_food()
        else:
            self.wait()
        
        
    def eat(self, meal):
        if self.food >=0 and meal<0:
            self.food += meal
        elif self.food < FOOD and meal>0:
            self.food += meal
            if self.food >FOOD:
                self.food = FOOD
    
    def life(self):
        if self.food<=0 and self.health > 0:
            self.health -= 1
            if self.food < 0.2*FOOD:
                self.state = State.COMING_BACK_COLONY
        elif self.food > 0 and self.health < HEALTH:
            self.health += 1
    
    def view_health(self):
        self.color = world_variables.ant_color
        if self.health < 30:
            self.color = world_variables.ant_trace_forward