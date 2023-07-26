import random
import math
import random
import pygame
from enum import Enum
from world_variables import World_Variables
from world import World
from obstacles import Obstacles

world_variables = World_Variables()
WIN_WIDTH, WIN_HEIGHT = world_variables.screenX, world_variables.screenY
HEALTH, FOOD = 30*30,30*120 #30*30, 30*120 
ANT_RADIUS = 2

class State (Enum):
    LOOKING_FOR_FOOD = 1
    COMING_BACK_COLONY = 2
    WAITING = 3
    CARRYING_FOOD = 4 
    GOING_FOR_FOOD = 5


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
        self.verify_direction(world_matrix)
            
        if self.distance < self.next_distance :
            self.x = self.x + self.speed * math.cos(self.angle)
            self.y = self.y + self.speed * math.sin(self.angle)
            self.distance += self.speed
        
        elif self.distance >= self.next_distance:
            self.distance = 0
            self.next_distance = random.uniform(10,30)
            self.angle = self.angle + random.uniform(-2,2)

    def go_to_colony(self,world_matrix):
        self.verify_direction(world_matrix)
        dx = (WIN_WIDTH // 2) - self.x
        dy = (WIN_HEIGHT // 2) - self.y
        if self.distance < self.next_distance and math.sqrt(dx**2 + dy**2) > 5:
            self.x = self.x + self.speed * math.cos(self.angle)
            self.y = self.y + self.speed * math.sin(self.angle)
            self.distance += self.speed
        elif self.distance >= self.next_distance and math.sqrt(dx**2 + dy**2) > 5:
            self.distance = 0
            self.next_distance = random.uniform(10,30)
            self.angle = math.atan2((WIN_HEIGHT // 2) - self.y, (WIN_WIDTH // 2) - self.x) + random.uniform(-1,1)
        else:
            if self.state == State.COMING_BACK_COLONY:
                self.state = State.LOOKING_FOR_FOOD
            elif self.state == State.CARRYING_FOOD:
                self.state = State.GOING_FOR_FOOD
            self.in_colony()

    def verify_direction(self,world_matrix):
        nextx = self.x + self.speed * math.cos(self.angle)
        nexty = self.y + self.speed * math.sin(self.angle)

        # If the ant hits the left or right edge of the screen, adjust its angle by π plus a random amount
        if nextx < ANT_RADIUS or nextx > WIN_WIDTH - ANT_RADIUS:
            self.angle = math.pi - self.angle

        # If the ant hits the top or bottom edge of the screen, flip the sign of its angle and add a random amount
        if nexty < ANT_RADIUS or nexty > WIN_HEIGHT - ANT_RADIUS:
            self.angle = -self.angle

        if world_matrix.verify(nextx, nexty):
            self.angle = (self.angle + math.pi) % (2 * math.pi)
        
            

    def in_colony(self):
        self.color = world_variables.ant_color
        self.food = FOOD
        
    
    def carry_food(self,world_matrix):
        self.go_to_colony()

    def move(self, world_matrix):
        if self.state == State.LOOKING_FOR_FOOD:
            self.look_for_food(world_matrix)
        elif self.state == State.COMING_BACK_COLONY:
            self.go_to_colony(world_matrix)
        elif self.state == State.CARRYING_FOOD:
            self.carry_food(world_matrix)
        else:
            pass
        
        
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