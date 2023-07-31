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
HEALTH, FOOD = 30*10,30*30 #30*30, 30*120 
ANT_RADIUS = 2

class State (Enum):
    LOOKING_FOR_FOOD = 1
    COMING_BACK_COLONY = 2
    WAITING = 3
    CARRYING_FOOD = 4 
    GOING_FOR_FOOD = 5
    KEEPING_TRACE = 6


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

    def move(self, world_matrix):
        if self.state == State.LOOKING_FOR_FOOD:
            self.look_for_food(world_matrix)
        elif self.state == State.COMING_BACK_COLONY:
            self.go_to_colony(world_matrix, False)
        elif self.state == State.CARRYING_FOOD:
            self.go_to_colony(world_matrix, True)
        elif self.state == State.GOING_FOR_FOOD:
            self.go_to_food(world_matrix)
        elif self.state == State.KEEPING_TRACE:
            pass
        else:
            pass

    def look_for_food(self,world_matrix):
        if self.distance < self.next_distance :
            self.x = self.x + self.speed * math.cos(self.angle)
            self.y = self.y + self.speed * math.sin(self.angle)
            self.distance += self.speed
        
        elif self.distance >= self.next_distance:
            self.distance = 0
            self.next_distance = random.uniform(10,30)
            self.angle = self.angle + random.uniform(-2,2)
        
        if self.x < WIN_WIDTH and self.x > 0 and self.y < WIN_HEIGHT and self.y > 0:
            world_matrix.world_matrix[int(self.y/4)][int(self.x/4)] = world_variables.ant_trace_forward
            world_matrix.world_matrix_id[int(self.y/4)][int(self.x/4)] = self.id

    def go_to_colony(self,world_matrix, carry_food):
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

        if self.x < WIN_WIDTH and self.x > 0 and self.y < WIN_HEIGHT and self.y > 0:
            world_matrix.world_matrix[int(self.y/4)][int(self.x/4)] = world_variables.ant_trace_back
            world_matrix.world_matrix_id[int(self.y/4)][int(self.x/4)] = self.id

    def verify_direction(self,world_matrix):
        nextx = self.x + self.speed * math.cos(self.angle)
        nexty = self.y + self.speed * math.sin(self.angle)

        if world_matrix.verify(nextx, nexty):
            self.angle = (self.angle + math.pi) % (2 * math.pi)
        
    def tracing_for_food(self,world_matrix):
        pass        

    def tracing_to_colony(self,world_matrix):
        pass

    def go_to_food(self, word_matrix):
        pass

    def in_colony(self):
        self.color = world_variables.ant_color
        self.food = FOOD
        

    def eat(self, meal):
        if self.food >=0 and meal<0:
            self.food += meal
        elif self.food < FOOD and meal>0:
            self.food += meal
            if self.food >FOOD:
                self.food = FOOD
    
    def life(self):
        if self.food<=0 and self.health > 0:
            self.health -= self.speed
            if self.food < 0.2*FOOD:
                self.state = State.COMING_BACK_COLONY
        elif self.food > 0 and self.health < HEALTH:
            self.health += 1
    
    def view_health(self):
        self.color = world_variables.ant_color
        if self.health < 30:
            self.color = world_variables.ant_trace_forward