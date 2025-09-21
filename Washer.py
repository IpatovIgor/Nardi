import math

import pygame


class Washer:
    normalImage = -1
    bigImage = -1
    image = -1
    size = 50
    x = 0
    y = 0

    def __init__(self, type: str, x: int, y: int):
        if type == "Black":
            self.normalImage = pygame.transform.scale(pygame.image.load("imeges/ФишкаЧёрная.png"),
                                                (self.size, self.size))
            self.bigImage = pygame.transform.scale(pygame.image.load("imeges/ФишкаЧёрная.png"),
                                                (self.size * 1.1, self.size * 1.1))
        elif type == "White":
            self.normalImage = pygame.transform.scale(pygame.image.load("imeges/ФишкаБелая.png"),
                                                (self.size, self.size))
            self.bigImage = pygame.transform.scale(pygame.image.load("imeges/ФишкаБелая.png"),
                                                (self.size * 1.1, self.size * 1.1))
        else:
            raise Exception("Неправильно указан цвет")
        self.whasher_rect = self.normalImage.get_rect(topleft=(x, y))
        self.x, self.y = x, y

    whasher_rect = -1
    state = "Small"

    def checkMousOnWasher(self):
        self.image = self.normalImage
        self.state = "Small"
        mouse = pygame.mouse.get_pos()
        if self.whasher_rect.collidepoint(mouse) and self.state == "Small":
            self.image = self.bigImage
            self.state = "Big"

    def printWasher(self, screen):
        self.checkMousOnWasher()
        screen.blit(self.image, (self.x, self.y))

    def moveTo(self, newX, newY, screen, dec, clock):
        deltaX = newX - self.x
        deltaY = newY - self.y
        length = math.sqrt(deltaX ** 2 + deltaY ** 2)
        deltaX /= length / 2
        deltaY /= length / 2
        for i in range(int(length // 2)):
            screen.blit(dec, (0, 0))
            self.x, self.y = self.x + deltaX, self.y + deltaY
            self.printWasher(screen)
            pygame.display.update()
            clock.tick(60)
        self.whasher_rect = self.image.get_rect(topleft=(self.x, self.y))
