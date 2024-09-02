import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot



def main():
        pygame.init()
        clock = pygame.time.Clock()
        dt = 0

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        
        updatable = pygame.sprite.Group()

        drawable = pygame.sprite.Group()

        asteroids = pygame.sprite.Group()

        shots = pygame.sprite.Group()

        Shot.containers = (shots, drawable, updatable)

        Asteroids.containers = (asteroids, drawable, updatable)

        AsteroidField.containers = (updatable)

        Player.containers = (updatable, drawable)


        player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)

        asteroidfield = AsteroidField()


# Main game loop:
        while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        return
                
              screen.fill("black")
              
              for item in updatable:
                    item.update(dt)
            
              for item in asteroids:
                    if item.collision(player) is True:
                          sys.exit("Game over!")
              

              for item in drawable:
                    item.draw(screen)
                     

              pygame.display.flip()


              dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()