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

    for i in range(5):
        particles.append(Particle(200, i*spacing))
        if i != 0:
            a = particles[i]
            b = particles[i-1]
            springs.append(Spring(k, spacing, a, b))

    return clock, screen


def draw(clock, screen):
    while True:
        screen.fill(pygame.Color((0, 0, 0)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        for spring in springs:
            spring.update()
            spring.draw(screen)

        for particle in particles:
            particle.update()
            particle.draw(screen, P_BLUE, 16)
            particle.draw(screen, ORANGE, 12)
        particles[4].draw(screen, P_GREEN, 16)
        particles[4].draw(screen, P_RED, 12)

        tail = particles[len(particles)-1]
        m_x, m_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            tail.position.x = m_x
            tail.position.y = m_y

        pygame.display.update()
        clock.tick(FPS)


def main():
    clock, screen = setup()
    draw(clock, screen)


if __name__ == '__main__':
    main()
