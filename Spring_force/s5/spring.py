import pygame
from settings import *


class Spring:
    def __init__(self, k, rest_length, a, b):
        self.k = k
        self.rest_length = rest_length
        self.a = a
        self.b = b

    def update(self):
        force = self.a.position - self.b.position
        x = force.magnitude() - self.rest_length
        force.normalize_ip()
        force *= (self.k * x)
        self.b.apply_force(force)
        force *= (-1)
        self.a.apply_force(force)

    def draw(self, screen):
        pygame.draw.lines(screen, ORANGE, False, (
            self.a.position.x, self.a.position.y),
            (self.b.position.x, self.b.position.y),
            width=3)
