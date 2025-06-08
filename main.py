# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    
    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0 , 0, 0))

        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()