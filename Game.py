import pygame
import random
from Washer import *
from Cube import *


def start_game(screen, clock):
    dec = pygame.transform.scale(
        pygame.image.load("imeges/доскаДляНардов.png"),
        (600, 600))
    running = True
    cube = Cube()
    base = Base(10, 10, 4, [])
    while running:
        screen.blit(dec, (0, 0))
        base.printWashers(screen)
        cube.prinCube(screen)
        pygame.display.update()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                cube.throw_cubs(screen, clock)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        clock.tick(15)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
start_game(screen, clock)
