from angry_boy import *
from cat import *

if __name__ == '__main__':
    print("Input number of task")
    print("1-Angry_Smile")
    print("2-One_cat")
    print("3-Cats_and_windows")
    task = int(input())
    if task == 1:
        screen = pygame.display.set_mode((500, 500))
        angry_boy(screen)
        some_function_done()
    elif task == 2:
        screen = pygame.display.set_mode((700, 700))
        cat_or_cats(screen, 1)
        some_function_done()
    else:
        screen = pygame.display.set_mode((700, 700))
        cat_or_cats(screen, 2)
        some_function_done()
