import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(angle) * 1.2
        new_velocity2 = self.velocity.rotate(-angle) * 1.2
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_rad)
        ast1.velocity = new_velocity1

        ast2 = Asteroid(self.position.x, self.position.y, new_rad)
        ast2.velocity = new_velocity2