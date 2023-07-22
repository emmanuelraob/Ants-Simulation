import pygame
import random
import math

# Define some constants
WIN_WIDTH, WIN_HEIGHT = 800, 600
FPS = 60
ANT_RADIUS = 5
SPEED = 1
N_OBSTACLES = 5  # The number of random obstacles
OBSTACLES = [pygame.Rect(random.randint(50, WIN_WIDTH-150), random.randint(50, WIN_HEIGHT-150), 100, 100) for _ in range(N_OBSTACLES)]  # A list of random obstacles

class Ant:
    def __init__(self, id):
        self.id = id
        self.x = WIN_WIDTH // 2 + random.randint(-10, 10)  # ants start near the center
        self.y = WIN_HEIGHT // 2 + random.randint(-10, 10)  # ants start near the center
        self.health = 100
        self.food = 0
        self.angle = random.uniform(0, 2*math.pi)  # ants start with a random orientation

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), ANT_RADIUS)

    def move(self):
        proposed_x = self.x + SPEED * math.cos(self.angle)
        proposed_y = self.y + SPEED * math.sin(self.angle)

        # Bounce off the edges and obstacles
        if proposed_x < ANT_RADIUS or proposed_x > WIN_WIDTH - ANT_RADIUS or any(obstacle.collidepoint(proposed_x, self.y) for obstacle in OBSTACLES):
            self.angle = math.pi - self.angle
        else:
            self.x = proposed_x

        if proposed_y < ANT_RADIUS or proposed_y > WIN_HEIGHT - ANT_RADIUS or any(obstacle.collidepoint(self.x, proposed_y) for obstacle in OBSTACLES):
            self.angle = -self.angle
        else:
            self.y = proposed_y

        self.angle += random.uniform(-0.1, 0.1)  # adjust orientation randomly

    def eat(self, amount):
        self.food -= amount
        self.health += amount

    def gather(self, amount):
        self.food += amount

class Colony:
    def __init__(self, size):
        self.size = size
        self.ants = [Ant(i) for i in range(size)]
        self.food = 1000

    def draw(self, win):
        for ant in self.ants:
            ant.draw(win)

    def feed_ants(self):
        for ant in self.ants:
            if self.food > 0 and ant.food < 50:
                food_to_give = min(50 - ant.food, self.food)
                ant.eat(food_to_give)
                self.food -= food_to_give

    def gather_food(self):
        for ant in self.ants:
            if ant.food > 0:
                food_to_gather = ant.food
                ant.gather(-food_to_gather)
                self.food += food_to_gather

    def move_ants(self):
        for ant in self.ants:
            ant.move()

def draw_window(win, colony):
    win.fill((255, 255, 255))  # Fill the screen with white
    for obstacle in OBSTACLES:
        pygame.draw.rect(win, (200, 200, 200), obstacle)  # Draw the obstacles
    colony.draw(win)  # Draw the colony
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

        colony.feed_ants()
        colony.gather_food()
        colony.move_ants()

        draw_window(win, colony)

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    run_simulation()
