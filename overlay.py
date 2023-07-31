import pygame
from world_variables import World_Variables
world_variables = World_Variables()

class Overlay:
    def __init__(self):
        self.rect = pygame.Rect(world_variables.screenX-world_variables.overlay_thickness, 0, world_variables.overlay_thickness, world_variables.screenY)
        self.left_space = world_variables.overlay_thickness - 20
        self.font = pygame.font.Font(None, 20)
        
        #variables to display
        self.ant_amount = 0
        self.colony_food = 0

        
    def update(self, colony):
        self.ant_amount = colony.size
        self.colony_food = colony.food

    def draw(self, win):
        self.text1 = self.font.render(f"Ant amount: {self.ant_amount}", True, (255, 255, 255))
        self.text2 = self.font.render(f"Colony food: {self.colony_food}", True, (255, 255, 255))
        self.text3 = self.font.render(f"Variable 3: {3}", True, (255, 255, 255))

        pygame.draw.rect(win, world_variables.obstacle_color, self.rect)

        win.blit(self.text1, (world_variables.screenX - self.left_space, 20))
        win.blit(self.text2, (world_variables.screenX - self.left_space, 50))  # Ajusta la posición y el espaciado según sea necesario
        win.blit(self.text3, (world_variables.screenX - self.left_space, 80))