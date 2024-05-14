import pygame
from settings import *
from particle import *
from spring import *


def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    bob = Particle(350, 300)
    anchor = Particle(300, 10)
    spring = Spring(0.01, 200, bob, anchor)

    return clock, screen, bob, anchor, spring


def draw(clock, screen, bob, anchor, spring):
    while True:
        screen.fill(pygame.Color((0, 0, 0)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        spring.draw(screen)
        spring.update()
        bob.draw(screen, P_RED, 42)
        bob.draw(screen, P_GREEN, 32)
        bob.update()
        anchor.draw(screen, ORANGE, 42)
        anchor.draw(screen, P_BLUE, 32)
        anchor.update()

        m_x, m_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            bob.position.x = m_x
            bob.position.y = m_y

        pygame.display.update()
        clock.tick(FPS)


def main():
    clock, screen,  bob, anchor, spring = setup()
    draw(clock, screen,  bob, anchor, spring)


if __name__ == '__main__':
    main()
