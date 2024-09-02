import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(surface = screen, color = "white", center = self.position, radius = self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            first_vector = self.velocity.rotate(random_angle)
            second_vector = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroids(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = first_vector * 1.2
            asteroid2 = Asteroids(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = second_vector * 1.2

