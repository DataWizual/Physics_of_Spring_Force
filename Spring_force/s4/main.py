import pygame
from settings import *
from particle import *
from spring import *

particles = []
springs = []


def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    for i in range(20):
        particles.append(Particle(200, i*spacing))
        if i != 0:
            a = particles[i]
            b = particles[i-1]
            springs.append(Spring(k, spacing, a, b))
    gravity = pygame.Vector2(0, 0.1)

    return clock, screen, gravity


def draw(clock, screen, gravity):
    while True:
        screen.fill(pygame.Color((0, 0, 0)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        for spring in springs:
            spring.update()
            spring.draw(screen)

        for particle in particles:
            particle.apply_force(gravity)
            particle.update()
            particle.draw(screen, P_BLUE, 8)
            particle.draw(screen, ORANGE, 4)
        particles[0].locked = True
        particles[0].draw(screen, P_GREEN, 8)
        particles[0].draw(screen, P_BLUE, 4)

        tail = particles[-1]
        m_x, m_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            tail.position.x = m_x
            tail.position.y = m_y

        pygame.display.update()
        clock.tick(FPS)


def main():
    clock, screen, gravity = setup()
    draw(clock, screen, gravity)


if __name__ == '__main__':
    main()
