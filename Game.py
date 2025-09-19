import pygame


def throw_kubs(screen, clock):
    stac = pygame.transform.scale(
        pygame.image.load("imeges/стакан.png"),
        (832 * 0.1, 1216 * 0.1))
    dec = pygame.transform.scale(
        pygame.image.load("imeges/доскаДляНардов.png"),
        (600, 600))
    for i in range(100):
        screen.blit(dec, (0, 0))
        screen.blit(stac, (100, 100 + (-1) ** i * 10))
        pygame.display.update()
        clock.tick(15)


def start_game(screen, clock):
    dec = pygame.transform.scale(
        pygame.image.load("imeges/доскаДляНардов.png"),
        (600, 600))
    running = True
    while running:
        screen.blit(dec, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                throw_kubs(screen, clock)
                pygame.quit()
                quit()

        clock.tick(15)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
start_game(screen, clock)
