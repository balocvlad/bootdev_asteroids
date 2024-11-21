import pygame
from constants import *
from circleshape import *
from player import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))


def main():
    pygame.init()
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill((250,128,114))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        player.update(dt)


    

if __name__ == "__main__":
    main()