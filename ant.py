import random
import math
import random
import pygame

WIN_WIDTH, WIN_HEIGHT = 800, 600
HEALTH, FOOD = 30*30, 30*120 #30*30, #30*120
ANT_RADIUS = 2

class Ant:
    def __init__(self, id, x=WIN_WIDTH/2 , y=WIN_HEIGHT/2 ):
        self.id = id
        self.x = x
        self.y = y
        self.health = HEALTH  # this amount of heath last for 30 seconds before the ant die
        self.food = FOOD # this amount of food last arround 2 minutes
        self.speed = random.uniform(0.5,1.5)
        self.angle = random.uniform(0, 2*math.pi)  # ants start with a random orientation
        self.color = (0,0,0)
        self.distance = 0
        self.next_distance = random.uniform(10,30) # to move in little lines
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), ANT_RADIUS)

    def move(self):
        if self.distance < self.next_distance :
            self.x = self.x + self.speed * math.cos(self.angle)
            self.y = self.y + self.speed * math.sin(self.angle)
            self.distance += self.speed
        
        elif self.distance >= self.next_distance:
            self.distance = 0
            self.next_distance = random.uniform(10,30)
            self.angle = self.angle + random.uniform(-2,2)

        # If the ant hits the left or right edge of the screen, adjust its angle by π plus a random amount
        if self.x < ANT_RADIUS or self.x > WIN_WIDTH - ANT_RADIUS:
            self.angle = math.pi - self.angle + random.uniform(-0.5, -0.5)

        # If the ant hits the top or bottom edge of the screen, flip the sign of its angle and add a random amount
        if self.y < ANT_RADIUS or self.y > WIN_HEIGHT - ANT_RADIUS:
            self.angle = -self.angle + random.uniform(-0.5, 0.5)


    def eat(self, meal):
        if self.food >=0 and meal<0:
            self.food += meal
        elif self.food < FOOD and meal>0:
            self.food += meal
            if self.food >FOOD:
                self.food = FOOD
    
    def life(self):
        if self.food<=0:
            self.health -= 1
    
    def view_health(self):
        if self.food <= 0:
            self.color = (255,0,0)