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
        particles.append(Particle(WIDTH//2, i*spacing))
        if i != 0:
            a = particles[i]
            b = particles[i-1]
            springs.append(Spring(k, spacing, a, b))
    gravity = pygame.Vector2(0, 0.1)
    return clock, screen, gravity


def draw(clock, screen, gravity):
    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        for spring in springs:
            spring.update()
        pygame.draw.lines(screen, P_GREEN, False, [
                          (particle.position.x, particle.position.y) for particle in particles], 8)
        pygame.draw.lines(screen, P_WHITE, False, [
                          (particle.position.x, particle.position.y) for particle in particles], 4)

        for particle in particles:
            particle.apply_force(gravity)
            particle.update()
        particles[0].locked = True

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
