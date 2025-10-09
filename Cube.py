import pygame
import random

class Cube:
    def __init__(self):
        self.imageE = pygame.transform.scale(pygame.image.load("imeges/E.png"), (60, 50))

    cube_list = [pygame.transform.scale(pygame.image.load("imeges/куб1.png"), (30, 30)),
                 pygame.transform.scale(pygame.image.load("imeges/куб2.png"), (30, 30)),
                 pygame.transform.scale(pygame.image.load("imeges/куб3.png"), (30, 30)),
                 pygame.transform.scale(pygame.image.load("imeges/куб4.png"), (30, 30)),
                 pygame.transform.scale(pygame.image.load("imeges/куб5.png"), (30, 30)),
                 pygame.transform.scale(pygame.image.load("imeges/куб6.png"), (30, 30))]

    def throw_cubs(self, screen, clock):
        stac = pygame.transform.scale(
            pygame.image.load("imeges/стакан.png"),
            (832 * 0.1, 1216 * 0.1))
        dec = pygame.transform.scale(
            pygame.image.load("imeges/доскаДляНардов.png"),
            (600, 600))
        for i in range(20):
            screen.blit(dec, (0, 0))
            screen.blit(stac, (100, 100 + (-1) ** i * 10))
            pygame.display.update()
            clock.tick(15)
        first, second = random.randint(1, 6), random.randint(1, 6)
        self.firstCube = first - 1
        self.secondCube = second - 1
        return [first, second]

    firstCube = 0
    secondCube = 0

    def prinCube(self, screen, was_thrown):
        screen.blit(self.cube_list[self.firstCube], (110, 110))
        screen.blit(self.cube_list[self.secondCube], (110, 160))
        if not was_thrown:
            screen.blit(self.imageE, (260, 540))