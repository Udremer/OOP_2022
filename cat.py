from math import pi
from window import *

pygame.init()


def draw_ellipse_angle(surface, color, rectan, angle, width=0):
    target_rect = pygame.Rect(rectan)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


# Draw a ball
def ball(x_start, y_start, screen):
    ellipse(screen, gray1, [x_start, y_start, 150, 80])
    ellipse(screen, black, [x_start, y_start, 150, 80], 1)
    arc(screen, (0, 0, 0), (x_start - 10, y_start + 5, 150, 80), 0, pi / 2)
    arc(screen, (0, 0, 0), (x_start - 30, y_start + 15, 150, 80), 0, pi / 2)
    arc(screen, (0, 0, 0), (x_start - 50, y_start + 20, 150, 80), 0, pi / 2)
    arc(screen, (0, 0, 0), (x_start + 25, y_start + 20, 150, 80), 2.1 * pi / 3, pi)
    arc(screen, (0, 0, 0), (x_start + 40, y_start + 25, 150, 80), 2.1 * pi / 3, pi)


# Drawing a cat with need size
def scale_cat(x_start, y_start, i, screen):
    i = i / 10
    x0 = 20
    y0 = 370
    x1 = - x0 * i + x_start
    y1 = - y0 * i + y_start
    # Drawing a tail
    draw_ellipse_angle(screen, brown_for_cat, [560 * i + x1, 440 * i + y1, 250 * i, 80 * i], -30)
    draw_ellipse_angle(screen, black, [560 * i + x1, 440 * i + y1, 250 * i, 80 * i], -30, 1)

    # Drawing a body of cat
    ellipse(screen, brown_for_cat, (100 * i + x1, 360 * i + y1, 530 * i, 165 * i))
    ellipse(screen, black, (100 * i + x1, 360 * i + y1, 530 * i, 165 * i), 1)

    # Drawing a paw
    ellipse(screen, brown_for_cat, (60 * i + x1, 430 * i + y1, 60 * i, 65 * i))
    ellipse(screen, black, (60 * i + x1, 430 * i + y1, 60 * i, 65 * i), 1)

    # Drawing a head
    ellipse(screen, brown_for_cat, (20 * i + x1, 375 * i + y1, 220 * i, 110 * i))
    ellipse(screen, black, (20 * i + x1, 375 * i + y1, 220 * i, 110 * i), 1)

    # Drawing a paws
    ellipse(screen, brown_for_cat, (130 * i + x1, 480 * i + y1, 130 * i, 50 * i))
    ellipse(screen, black, (130 * i + x1, 480 * i + y1, 130 * i, 50 * i), 1)
    ellipse(screen, brown_for_cat, (450 * i + x1, 425 * i + y1, 180 * i, 115 * i))
    ellipse(screen, black, (450 * i + x1, 425 * i + y1, 180 * i, 115 * i), 1)
    ellipse(screen, brown_for_cat, (607 * i + x1, 480 * i + y1, 50 * i, 90 * i))
    ellipse(screen, black, (607 * i + x1, 480 * i + y1, 50 * i, 90 * i), 1)

    # Drawing ears
    polygon(screen, brown_for_cat, [(x_start, y_start), (63 * i + x1, 392 * i + y1), (30 * i + x1, 410 * i + y1)])
    polygon(screen, black, [(x_start, y_start), (63 * i + x1, 392 * i + y1), (30 * i + x1, 410 * i + y1)], 1)
    polygon(screen, in_ears, [(27 * i + x1, 377 * i + y1), (55 * i + x1, 392 * i + y1), (34 * i + x1, 403 * i + y1)])
    polygon(screen, black, [(27 * i + x1, 377 * i + y1), (55 * i + x1, 392 * i + y1), (34 * i + x1, 403 * i + y1)],
            1)
    polygon(screen, brown_for_cat,
            [(210 * i + x1, 355 * i + y1), (197 * i + x1, 395 * i + y1), (160 * i + x1, 382 * i + y1)])
    polygon(screen, black, [(210 * i + x1, 355 * i + y1), (197 * i + x1, 395 * i + y1), (160 * i + x1, 382 * i + y1)],
            1)
    polygon(screen, in_ears, [(202 * i + x1, 363 * i + y1), (192 * i + x1, 388 * i + y1), (172 * i + x1, 381 * i + y1)])
    polygon(screen, black, [(202 * i + x1, 363 * i + y1), (192 * i + x1, 388 * i + y1), (172 * i + x1, 381 * i + y1)],
            1)

    # Drawing eyes
    ellipse(screen, eye, (55 * i + x1, 410 * i + y1, 55 * i, 40 * i))
    ellipse(screen, black, (55 * i + x1, 410 * i + y1, 55 * i, 40 * i), 1)
    ellipse(screen, eye, (150 * i + x1, 410 * i + y1, 55 * i, 40 * i))
    ellipse(screen, black, (150 * i + x1, 410 * i + y1, 55 * i, 40 * i), 1)
    ellipse(screen, black, (85 * i + x1, 410 * i + y1, 10 * i, 40 * i))
    ellipse(screen, black, (180 * i + x1, 410 * i + y1, 10 * i, 40 * i))
    draw_ellipse_angle(screen, white, [73 * i + x1, 410 * i + y1, 8 * i, 20 * i], 220, 0)
    draw_ellipse_angle(screen, white, [168 * i + x1, 410 * i + y1, 8 * i, 20 * i], 220, 0)

    # Drawing a nose
    polygon(screen, in_ears, [(127 * i + x1, 450 * i + y1), (139 * i + x1, 450 * i + y1), (127 * i + x1, 457 * i + y1),
                              (115 * i + x1, 450 * i + y1)])
    polygon(screen, black,
            [(127 * i + x1, 450 * i + y1), (139 * i + x1, 450 * i + y1), (127 * i + x1, 457 * i + y1),
             (115 * i + x1, 450 * i + y1)], 1)
    line(screen, black, (127 * i + x1, 457 * i + y1), (127 * i + x1, 467 * i + y1), 1)

    # Drawing a mouth
    arc(screen, black, [127 * i + x1, 462 * i + y1, 16 * i, 10 * i], pi, 15 * pi / 8)
    arc(screen, black, [111 * i + x1, 462 * i + y1, 16 * i, 10 * i], pi, 15 * pi / 8)

    # Drawing a moustache
    arc(screen, black, [-80 * i + x1, 444 * i + y1, 700 * i, 500 * i], 1.55, 1.9)
    arc(screen, black, [-78 * i + x1, 455 * i + y1, 700 * i, 200 * i], 1.55, 1.9)
    arc(screen, black, [-145 * i + x1, 463 * i + y1, 700 * i, 200 * i], 1.3, 1.7)
    arc(screen, black, [-375 * i + x1, 440 * i + y1, 700 * i, 500 * i], 1.2, 1.65)
    arc(screen, black, [-410 * i + x1, 448 * i + y1, 700 * i, 200 * i], 1.1, 1.5)
    arc(screen, black, [-345 * i + x1, 460 * i + y1, 700 * i, 200 * i], 1.3, 1.75)


# Draw cnt_of_cats cats with ball
def cat_in_position(cnt_of_cats, screen):
    if cnt_of_cats < 0 or cnt_of_cats > 10:
        print("Number of cats cant be more then 6,or less then 0")
    else:
        if cnt_of_cats == 1:
            scale_cat(80, 370, 7, screen)
            ball(550, 600, screen)
        elif cnt_of_cats == 2:
            scale_cat(10, 450, 2, screen)
            scale_cat(200, 370, 7, screen)
            ball(550, 600, screen)
        elif cnt_of_cats == 3:
            scale_cat(10, 450, 2, screen)
            scale_cat(200, 370, 7, screen)
            scale_cat(150, 500, 4, screen)
            ball(550, 600, screen)
        elif cnt_of_cats == 4:
            scale_cat(10, 450, 2, screen)
            scale_cat(200, 370, 7, screen)
            scale_cat(150, 500, 4, screen)
            scale_cat(310, 585, 2, screen)
            ball(550, 600, screen)
        elif cnt_of_cats == 5:
            scale_cat(10, 450, 2, screen)
            scale_cat(200, 370, 7, screen)
            scale_cat(150, 500, 4, screen)
            scale_cat(310, 585, 2, screen)
            scale_cat(50, 600, 1, screen)
            ball(550, 600, screen)
        elif cnt_of_cats == 6:
            scale_cat(10, 450, 2, screen)
            scale_cat(200, 370, 7, screen)
            scale_cat(150, 500, 4, screen)
            scale_cat(310, 585, 2, screen)
            scale_cat(50, 600, 1, screen)
            scale_cat(20, 300, 3, screen)
            ball(550, 600, screen)
        elif cnt_of_cats == 7:
            scale_cat(10, 450, 2, screen)
            scale_cat(200, 370, 7, screen)
            scale_cat(150, 500, 4, screen)
            scale_cat(310, 585, 2, screen)
            scale_cat(50, 600, 1, screen)
            scale_cat(20, 300, 3, screen)
            scale_cat(150, 600, 1, screen)
            ball(550, 600, screen)
        elif cnt_of_cats == 8:
            scale_cat(10, 450, 2, screen)
            scale_cat(200, 370, 7, screen)
            scale_cat(150, 500, 4, screen)
            scale_cat(310, 585, 2, screen)
            scale_cat(50, 600, 1, screen)
            scale_cat(20, 300, 3, screen)
            scale_cat(150, 600, 2, screen)
            scale_cat(500, 310, 3, screen)
            ball(550, 600, screen)
        else:
            scale_cat(10, 450, 2, screen)
            scale_cat(200, 370, 7, screen)
            scale_cat(150, 500, 4, screen)
            scale_cat(310, 585, 2, screen)
            scale_cat(50, 600, 1, screen)
            scale_cat(20, 300, 3, screen)
            scale_cat(150, 600, 2, screen)
            scale_cat(500, 310, 3, screen)
            scale_cat(350, 310, 2, screen)
            ball(550, 600, screen)


def cat_or_cats(screen, num_task):
    rect(screen, brown_high, [0, 0, 700, 300])
    rect(screen, brown_low, [0, 300, 700, 400])
    if num_task == 1:
        windows = 1
        window_in_position(screen, windows)
        cats = 1
        cat_in_position(cats, screen)
    else:
        print("How many windows you want to draw?")
        print("You can draw 1,2,3 or 4 windows")
        windows = int(input("Enter number of windows "))
        window_in_position(screen, windows)
        print("How many cats you want to draw?")
        cats = int(input("Enter number of cats "))
        cat_in_position(cats, screen)
