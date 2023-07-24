import pygame

from ant import Ant
from colony import Colony
from food import Food
from world_variables import World_Variables

# Define some constants
world = World_Variables() # for use a group of globar variables used in all the program
WIN_WIDTH, WIN_HEIGHT = world.screenX, world.screenY
FPS = world.fps

def draw_window(win,colony, food, world_matrix):
    win.fill((255, 255, 255))  # Fill the screen with white
    world_matrix.draw(win)
    pygame.draw.circle(win, (100, 50, 0), (WIN_WIDTH // 2, WIN_HEIGHT // 2), 20)
    food.draw(win)
    colony.draw(win)
    pygame.display.update()  # Update the screen

def run_simulation():
    pygame.init()  # Initialize Pygame
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Create the Pygame window
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    world_matrix = World_Variables()
    colony = Colony(100)
    food = Food()
    run = True
    while run:
        clock.tick(FPS)  # Ensure the program runs at the same speed on all computers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        colony.move_ants(world_matrix)
        colony.eat_once()
        colony.view_health()
        colony.life()

        draw_window(win,colony,food,world_matrix)

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    run_simulation()
