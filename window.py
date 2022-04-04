from pygame.draw import *
from variables import *


# Draw 1 or 2 big window
def part1_of_window(x_start, y_start, screen):
    rect(screen, window_blue_light, [x_start, y_start, 280, 280])
    rect(screen, window_blue_dark, [x_start + 10, y_start + 5, 125, 80])
    rect(screen, window_blue_dark, [x_start + 145, y_start + 5, 125, 80])
    rect(screen, window_blue_dark, [x_start + 10, y_start + 95, 125, 180])
    rect(screen, window_blue_dark, [x_start + 145, y_start + 95, 125, 180])


# Draw 3 or 4 windows
def part2_of_window(x_start, y_start, screen):
    rect(screen, window_blue_light, [x_start, y_start, 160, 160])
    rect(screen, window_blue_dark, [x_start + 5, y_start + 5, 70, 50])
    rect(screen, window_blue_dark, [x_start + 85, y_start + 5, 70, 50])
    rect(screen, window_blue_dark, [x_start + 5, y_start + 65, 70, 90])
    rect(screen, window_blue_dark, [x_start + 85, y_start + 65, 70, 90])


# Draw cnt_window window
def window_in_position(screen, cnt_windows):
    if cnt_windows < 0 or cnt_windows > 4:
        print("Nuber of windows cant be less then 0 or more then 4")
    else:
        if cnt_windows == 1:
            part1_of_window(410, 10, screen)

        elif cnt_windows == 2:
            # Draw right window
            part1_of_window(410, 10, screen)
            # Draw left window
            part1_of_window(5, 10, screen)
        elif cnt_windows == 3:
            # Draw left window
            part2_of_window(5, 10, screen)
            # part2_of_window(180, 10, screen)
            # Draw center window
            part2_of_window(270, 10, screen)
            # Draw right window
            part2_of_window(530, 10, screen)
        else:
            part2_of_window(5, 10, screen)
            part2_of_window(180, 10, screen)
            part2_of_window(355, 10, screen)
            part2_of_window(530, 10, screen)
