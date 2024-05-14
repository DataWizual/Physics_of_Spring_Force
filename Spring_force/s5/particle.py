import pygame
from settings import *


class Particle:
    def __init__(self, x, y):
        self.locked = False
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0.05)
        self.mass = 1

    def apply_force(self, force):
        self.acceleration += (force.copy()/self.mass)

    def update(self):
        if not self.locked:
            self.velocity *= 0.99
            self.velocity += self.acceleration
            self.position += self.velocity
            self.acceleration *= 0

    def draw(self, screen):
        pygame.draw.circle(
            screen, P_BLUE, (int(self.position.x),
                             int(self.position.y)), 8)
