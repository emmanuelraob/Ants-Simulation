import random
import math
import random
import pygame

WIN_WIDTH, WIN_HEIGHT = 800, 600
ANT_RADIUS = 2
SPEED = 1

class Ant:
    def __init__(self, id, x=WIN_WIDTH/2 , y=WIN_HEIGHT/2 ):
        self.id = id
        self.x = x
        self.y = y
        self.health = 100
        self.food = 100
        self.speed = random.uniform(0.5,1.5)
        self.angle = random.uniform(0, 2*math.pi)  # ants start with a random orientation
        self.color = (0,0,0)
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), ANT_RADIUS)

    def move(self):
        proposed_x = self.x + self.speed * math.cos(self.angle)
        proposed_y = self.y + self.speed * math.sin(self.angle)

        # If the ant hits the left or right edge of the screen, adjust its angle by π plus a random amount
        if proposed_x < ANT_RADIUS or proposed_x > WIN_WIDTH - ANT_RADIUS:
            self.angle = math.pi - self.angle + random.uniform(-0.5, 0.5)

        # If the ant hits the top or bottom edge of the screen, flip the sign of its angle and add a random amount
        if proposed_y < ANT_RADIUS or proposed_y > WIN_HEIGHT - ANT_RADIUS:
            self.angle = -self.angle + random.uniform(-0.5, 0.5)

        # Update the ant's position using the (possibly updated) angle
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

        # Ensure the angle stays within the range [0, 2π)
        self.angle = self.angle % (2 * math.pi)

    def eat(self, meal):
        if self.food >=0 and meal<0:
            self.food += meal
        elif self.food < 100 and meal>0:
            self.food += meal
            if self.food >100:
                self.food = 100
    
    def life(self):
        if self.food<=0:
            self.health =- 1
    
    def view_health(self):
        if self.health <= 0:
            self.color = (255,0,0)
            self.color = (0,self.food*2,0)
        else:
            self.color = (0,0,0)