import pygame
from constants import *

# this is where you define the function
def main():
    #initialize all imported pygame modules
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

# this is where you call the function
if __name__ == "__main__":
    main()