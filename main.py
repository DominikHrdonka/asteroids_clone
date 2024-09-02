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

        total_score = 0

        font = pygame.font.Font(None, 74)
      


# Main game loop:
        while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        return
                
              screen.fill("black")
              text = font.render((f"Total score: {total_score}"), True, "white")
              screen.blit(text, (100, 250))
              
              for item in updatable:
                    item.update(dt)
            
              for item in asteroids:
                    if item.collision(player) is True:
                          sys.exit("Game over!")
                    for shot in shots:
                          if shot.collision(item) is True:
                                shot.kill()
                                item.split()
                                total_score += 1
                                print(total_score)

              

              for item in drawable:
                    item.draw(screen)
                     

              pygame.display.flip()


              dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()