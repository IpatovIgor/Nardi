import pygame
import random
import math
from Cube import *


def reset_all():
    global moveIsGoing
    global moveColor
    global baseList
    global cubes_num
    global move_index
    global cubs_was_trow
    global count_of_black
    global count_of_white
    moveIsGoing = False
    moveColor = "Black"
    baseList = []
    cubes_num = [1, 1]
    move_index = 0
    cubs_was_trow = False
    count_of_black = 0
    count_of_white = 0


class SkipButton:
    def __init__(self):
        self.small_image = pygame.transform.scale(pygame.image.load("imeges/skip.png"), (40, 30))
        self.big_image = pygame.transform.scale(pygame.image.load("imeges/skip.png"), (57, 45))
        self.image = self.small_image
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.state = "Small"

    def check_mouse(self):
        global moveIsGoing
        global move_index
        global moveColor
        global cubs_was_trow
        self.image = self.small_image
        self.state = "Small"
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse) and self.state == "Small" and not moveIsGoing:
            self.image = self.big_image
            self.state = "Big"
        if self.rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] and cubs_was_trow:
            move_index = 0
            cubs_was_trow = False
            if moveColor == "Black":
                moveColor = "White"
            else:
                moveColor = "Black"
        self.print_button()

    def print_button(self):
        global screen
        screen.blit(self.image, (0, 0))


def can_move(washser, count, index_of_base):
    global moveIsGoing
    global baseList
    global move_index
    global cubes_num
    global moveColor
    global cubs_was_trow
    global count_of_black
    global count_of_white

    if washser.color == "Black":
        save_base = baseList[0]
    else:
        save_base = baseList[25]

    if save_base.count > 0:
        if washser.base.num != save_base.num:
            return False

    if moveIsGoing:
        return False

    if washser.index + 1 != washser.base.count:
        return False

    if 1 > index_of_base + count or index_of_base + count > 24:
        washser.base.pop_washer()
        if moveColor == "Black":
            count_of_black += 1
        else:
            count_of_white += 1
        move_index += 1
        if move_index == 2:
            move_index = 0
            cubs_was_trow = False
            if moveColor == "Black":
                moveColor = "White"
            else:
                moveColor = "Black"
        return False

    next_base = baseList[index_of_base + count]
    if next_base.count > 1 and next_base.washers[0].color != washser.color:
        return False
    if next_base.count == 1 and next_base.washers[0].color != washser.color:
        if next_base.washers[0].color == "Black":
            save_base = baseList[0]
        else:
            save_base = baseList[25]
        next_base.washers[0].base = save_base
        next_base.washers[0].x = save_base.x
        next_base.washers[0].y = save_base.y + 50 * save_base.count
        next_base.washers[0].index = save_base.count
        next_base.washers[0].whasher_rect = next_base.washers[0].image.get_rect(
            topleft=(save_base.x, save_base.y + 50 * save_base.count))
        save_base.addWasher(next_base.washers[0])
        next_base.pop_washer()
    return True


class Washer:
    normalImage = -1
    bigImage = -1
    size = 50
    direction = 0

    def __init__(self, type: str, x: int, y: int, base, index: int):
        self.color = type
        self.index = index
        if type == "Black":
            self.normalImage = pygame.transform.scale(pygame.image.load("imeges/ФишкаЧёрная.png"),
                                                (self.size, self.size))
            self.bigImage = pygame.transform.scale(pygame.image.load("imeges/ФишкаЧёрная.png"),
                                                (self.size * 1.1, self.size * 1.1))
            self.direction = 1
        elif type == "White":
            self.normalImage = pygame.transform.scale(pygame.image.load("imeges/ФишкаБелая.png"),
                                                (self.size, self.size))
            self.bigImage = pygame.transform.scale(pygame.image.load("imeges/ФишкаБелая.png"),
                                                (self.size * 1.1, self.size * 1.1))
            self.direction = -1
        else:
            raise Exception("Неправильно указан цвет")
        self.whasher_rect = self.normalImage.get_rect(topleft=(x, y))
        self.x, self.y = x, y
        self.base = base
        self.image = self.normalImage
        self.nextBase = base

    whasher_rect = -1
    state = "Small"
    base = -1
    index = -1
    nextBase = -1

    def checkMousOnWasher(self, screen):
        global moveIsGoing
        global baseList
        global cubes_num
        global move_index
        global cubs_was_trow
        self.image = self.normalImage
        self.state = "Small"
        if not cubs_was_trow:
            return

        mouse = pygame.mouse.get_pos()
        if self.whasher_rect.collidepoint(mouse) and self.state == "Small" and not moveIsGoing:
            self.image = self.bigImage
            self.state = "Big"

        if not moveIsGoing and self.whasher_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            if can_move(self, cubes_num[move_index] * self.direction, self.base.num):
                self.nextBase = baseList[(self.base.num
                                          + cubes_num[move_index] * self.direction)]
                moveIsGoing = True
                self.changeBase(self.nextBase)
                self.whasherIsGoing = True
        if self.whasherIsGoing:
            if self.nextBase.der == 'Down':
                self.moveTo(self.nextBase.x, self.base.y + (self.nextBase.count - 1) * 50)
            else:
                self.moveTo(self.nextBase.x, self.base.y - (self.nextBase.count - 1) * 50)

    def changeBase(self, newBase):
        self.base.washers.pop(-1)
        self.base.count -= 1
        self.index = len(newBase.washers)
        self.base = newBase
        self.base.addWasher(self)

    def printWasher(self, screen):
        global moveIsGoing
        if moveColor == self.color:
            self.checkMousOnWasher(screen)
        screen.blit(self.image, (self.x, self.y))

    whasherIsGoing = False

    def moveTo(self, nextX, nextY):
        global moveIsGoing
        global cubes_num
        global move_index

        deltaX = nextX - self.x
        deltaY = nextY - self.y
        length = math.sqrt(deltaX ** 2 + deltaY ** 2) / 5
        if length / 2 == 0:
            print(cubes_num[move_index])
            raise Exception("0")
        deltaX /= length
        deltaY /= length
        self.x, self.y = self.x + deltaX, self.y + deltaY
        if length < 1:
            self.x, self.y = nextX, nextY
        self.whasher_rect = self.image.get_rect(topleft=(self.x, self.y))
        if self.x == nextX and self.y == nextY:
            moveIsGoing = False
            self.whasherIsGoing = False


moveIsGoing = False
moveColor = "Black"


class Base:
    x = 0
    y = 0
    count = 0

    def __init__(self, x, y, num, der):
        self.num = num
        self.der = der
        global baseList
        baseList.append(self)
        self.baseList = baseList
        self.x, self.y = x, y
        self.washers = []

    def printWashers(self, screen):
        for washer in self.washers:
            washer.printWasher(screen)

    def addWasher(self, washer):
        self.washers.append(washer)
        self.count += 1

    def pop_washer(self):
        self.washers.pop(-1)
        self.count -= 1


baseList = []
cubes_num = [1, 1]


def init_bases():
    global baseList
    Base(530, 0, 0, "Down")

    for i in range(6):
        Base(505 - 39 * i, 500, i + 1, "Up")
    for i in range(6):
        Base(240 - 39 * i, 500, 7 + i, "Up")
    for i in range(6):
        Base(43 + 39 * i, 48, 13 + i, "Down")
    for i in range(6):
        Base(310 + 39 * i, 48, 19 + i, "Down")
    for i in range(2):
        baseList[1].addWasher(Washer("Black", 505, 500 - 50 * i, baseList[1], i))
        baseList[24].addWasher(Washer("White", 310 + 39 * 5, 48 + 50 * i, baseList[24], i))
    for i in range(5):
        baseList[6].addWasher(Washer("White", 505 - 39 * 5, 500 - 50 * i, baseList[6], i))
        baseList[19].addWasher(Washer("Black", 310, 48 + 50 * i, baseList[19], i))
        baseList[12].addWasher(Washer("Black", 240 - 39 * 5, 500 - 50 * i, baseList[12], i))
        baseList[13].addWasher(Washer("White", 43, 48 + 50 * i, baseList[13], i))
    for i in range(3):
        baseList[8].addWasher(Washer("White", 240 - 39, 500 - 50 * i, baseList[8], i))
        baseList[17].addWasher(Washer("Black", 43 + 39 * 4, 48 + 50 * i, baseList[17], i))
    Base(0, 20, 25, "Down")


move_index = 0
cubs_was_trow = False
count_of_black = 0
count_of_white = 0


def start_game(my_screen, my_clock):
    global cubes_num
    global screen
    global clock
    global cubs_was_trow
    global baseList
    global moveColor
    global moveIsGoing
    global move_index
    global count_of_black
    global count_of_white
    screen = my_screen
    clock = my_clock
    reset_all()
    dec = pygame.transform.scale(
        pygame.image.load("imeges/доскаДляНардов.png"),
        (600, 600))
    running = True
    cube = Cube()
    init_bases()
    skip_butt = SkipButton()
    wasMove = False
    while running:
        screen.blit(dec, (0, 0))
        skip_butt.check_mouse()

        if count_of_black >= 7 and not moveIsGoing:
            return "Black"
        if count_of_white >= 7 and not moveIsGoing:
            return "White"

        if moveIsGoing and wasMove is False:
            wasMove = True
        elif not moveIsGoing and wasMove is True:
            wasMove = False
            move_index += 1
            if move_index == 2:
                move_index = 0
                if moveColor == "Black":
                    moveColor = "White"
                else:
                    moveColor = "Black"
                cubs_was_trow = False

        for base in baseList:
            base.printWashers(screen)
        cube.prinCube(screen, cubs_was_trow)
        pygame.display.update()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e] and not cubs_was_trow:
                cubes_num = cube.throw_cubs(screen, clock)
                cubs_was_trow = True
            if keys[pygame.K_ESCAPE]:
                return "None"
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        clock.tick(60)


screen = -1
clock = -1
