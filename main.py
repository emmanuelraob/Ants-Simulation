import pygame

from ant import Ant
from colony import Colony

# Define some constants
WIN_WIDTH, WIN_HEIGHT = 800, 600
FPS = 30

def draw_window(win,colony):
    win.fill((255, 255, 255))  # Fill the screen with white
    colony.draw(win)
    pygame.display.update()  # Update the screen

def run_simulation():
    pygame.init()  # Initialize Pygame
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Create the Pygame window
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate

    colony = Colony(100)
    
    frame_count = 0

    run = True
    while run:
        clock.tick(FPS)  # Ensure the program runs at the same speed on all computers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        colony.move_ants()
        draw_window(win,colony)

        if frame_count >= FPS/2:
            colony.eat_once()
            colony.view_health()
            frame_count = 0

        colony.life()

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    run_simulation()
