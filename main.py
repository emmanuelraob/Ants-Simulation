import pygame

from ant import Ant
from colony import Colony

# Define some constants
WIN_WIDTH, WIN_HEIGHT = 800, 600
FPS = 30

def draw_window(win,colony):
    win.fill((255, 255, 255))  # Fill the screen with white
    pygame.draw.circle(win, (100, 50, 0), (WIN_WIDTH // 2, WIN_HEIGHT // 2), 20)
    colony.draw(win)
    pygame.display.update()  # Update the screen

def run_simulation():
    pygame.init()  # Initialize Pygame
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Create the Pygame window
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate

    colony = Colony(100)

    run = True
    while run:
        clock.tick(FPS)  # Ensure the program runs at the same speed on all computers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        colony.move_ants()
        draw_window(win,colony)
        colony.eat_once()
        colony.view_health()
        colony.life()

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    run_simulation()
