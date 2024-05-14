import pygame
from settings import *


def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(0)
    velocity = pygame.Vector2(0, 0)

    bob = pygame.Vector2(350, 250)

    anchor = pygame.Vector2(300, 10)

    gravity = pygame.Vector2(0, 1)

    return clock, screen, velocity, bob, anchor, gravity


def draw(clock, screen, velocity, bob, anchor, gravity):
    while True:
        screen.fill(pygame.Color((0, 0, 0)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        force = bob - anchor

        x = force.magnitude() - length

        force.normalize_ip()

        force *= (-1 * k * x)

        pygame.draw.line(screen, P_WHITE, start_pos=(
            anchor.x, anchor.y), end_pos=(bob.x, bob.y), width=3)
        pygame.draw.circle(screen, P_BLUE, (int(anchor.x), int(anchor.y)), 16)
        pygame.draw.circle(screen, ORANGE, (int(anchor.x), int(anchor.y)), 10)
        pygame.draw.circle(screen, P_BLUE, (int(bob.x), int(bob.y)), 32)
        pygame.draw.circle(screen, ORANGE, (int(bob.x), int(bob.y)), 26)

        m_x, m_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            bob.x = m_x
            bob.y = m_y

        velocity += force
        velocity += gravity
        bob += velocity
        velocity *= 0.99

        pygame.display.update()
        clock.tick(FPS)


def main():
    clock, screen, velocity, bob, anchor, gravity = setup()
    draw(clock, screen, velocity, bob, anchor, gravity)


if __name__ == '__main__':
    main()
