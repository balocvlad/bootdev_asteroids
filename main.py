import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = updatable

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))


def main():
    pygame.init()

    

    asteroid_filed = AsteroidField()    
    
    while True:
        global dt
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

        screen.fill((250,128,114))
        #player.draw(screen)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #player.update(dt)
       


    

if __name__ == "__main__":
    main()