import pygame

from colony.colony import Colony
from world.world import World
from world.world_variables import World_Variables
from overlay.overlay import Overlay

# Define some constants
world_variables = World_Variables() # for use a group of globar variables used in all the program
WIN_WIDTH, WIN_HEIGHT = world_variables.screenX, world_variables.screenY
FPS = world_variables.fps

def draw_window(win,colony, overlay, world_matrix):
    world_matrix.draw(win)
    pygame.draw.circle(win, (100, 50, 0), (WIN_WIDTH // 2, WIN_HEIGHT // 2), 20)
    colony.draw(win)
    overlay.draw(win)
    pygame.display.update()  # Update the screen


def run_simulation():
    pygame.init()  # Initialize Pygame
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Create the Pygame window
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    world_matrix = World()
    colony = Colony(world_variables.ant_amount)
    overlay = Overlay()
    run = True
    counter = 0
    while run:
        clock.tick(FPS)  # Ensure the program runs at the same speed on all computers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        colony.move_ants(world_matrix)
        colony.life()

        if counter == 0: #to do something once a second 
            overlay.update(colony)
            colony.spawn()
        if counter%5 == 0: #to do 6 times in a second 
            colony.view_health()
            
        draw_window(win,colony, overlay,world_matrix)

        counter = 0 if counter > world_variables.fps else counter + 1


    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    run_simulation()
