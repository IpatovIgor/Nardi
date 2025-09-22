import math
import pygame


class Washer:
    normalImage = -1
    bigImage = -1
    image = -1
    size = 50
    x = 0
    y = 0

    def __init__(self, type: str, x: int, y: int, base, index: int):
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
        self.base = base
        self.index = index

    whasher_rect = -1
    state = "Small"
    base = -1
    index = -1

    def checkMousOnWasher(self, screen):
        self.image = self.normalImage
        self.state = "Small"
        mouse = pygame.mouse.get_pos()
        if self.whasher_rect.collidepoint(mouse) and self.state == "Small":
            self.image = self.bigImage
            self.state = "Big"
        if self.whasher_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if not self.whasherIsGoing:
                self.moveTo(screen, self.base)

    def printWasher(self, screen):
        self.checkMousOnWasher(screen)
        screen.blit(self.image, (self.x, self.y))

    whasherIsGoing = False

    def moveTo(self, screen, nextBase):
        #if self.index + 1 != self.base.count:
        #    return

        dec = pygame.transform.scale(
            pygame.image.load("imeges/доскаДляНардов.png"),
            (600, 600))
        clock = pygame.time.Clock()
        self.base.washers.pop(-1)
        self.base.count -= 1
        self.base = nextBase
        self.base.addWasher(self)

        deltaX = nextBase.x - self.x
        deltaY = nextBase.count * 50
        length = math.sqrt(deltaX ** 2 + deltaY ** 2)
        if length / 2 == 0:
            print(nextBase.count)
            raise Exception("0")
        deltaX /= length / 2
        deltaY /= length / 2
        self.whasherIsGoing = True
        for i in range(int(length // 2)):
            screen.blit(dec, (0, 0))
            self.x, self.y = self.x + deltaX, self.y + deltaY
            self.printWasher(screen)
            pygame.display.update()
            clock.tick(60)
        self.whasherIsGoing = False
        self.whasher_rect = self.image.get_rect(topleft=(self.x, self.y))


class Base:
    x = 0
    y = 0
    washers = []
    baseList = []
    count = 0

    def __init__(self, x, y, count, baseList):
        baseList.append(self)
        self.baseList = baseList
        self.x, self.y = x, y
        for i in range(count):
            self.washers.append(Washer("Black", x, 50 * i, self, i + 1))
        self.count = count

    def printWashers(self, screen):
        for washer in self.washers:
            washer.printWasher(screen)

    def addWasher(self, washer):
        self.washers.append(washer)
