import pygame

FPS = 30
some_red = (252, 75, 50)
black = (0, 0, 0)
yellow = (213, 218, 18)
gray = (172, 172, 172)
white = (255, 255, 255)
brown_high = (85, 68, 0)
brown_low = (128, 102, 0)
window_blue_light = (213, 255, 230)
window_blue_dark = (135, 205, 222)
brown_for_cat = (200, 113, 55)
eye = (136, 170, 0)
ears = (250, 200, 167)
gray1 = (153, 153, 153)
in_ears = (250, 180, 240)


def some_function_done():
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    pygame.quit()
