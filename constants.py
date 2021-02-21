import os
import time
from colorama import init, Fore, Back, Style
init()

small_paddle_size = 10
paddle_size = 14
Ex_paddle_size = 20
timer_time = 10
total_bricks = 15
dims = os.get_terminal_size()
screen_ht = 50  # height of terminal
screen_wd = dims[0]  # width of terminal
game_ht = (0, screen_ht)  # height range of game in total screen
# width range of game in total screen
game_wd = (int(screen_wd/6), int(screen_wd - int(screen_wd/5)))
paddle_row = screen_ht-2
ball_row = paddle_row-1


'''
..####....####...##...##..######...........####...##..##..######..#####..........
.##......##..##..###.###..##..............##..##..##..##..##......##..##.........
.##.###..######..##.#.##..####............##..##..##..##..####....#####..........
.##..##..##..##..##...##..##..............##..##...####...##......##..##.........
..####...##..##..##...##..######...........####.....##....######..##..##.........
.................................................................................

'''


def over(score):
    os.system('clear')
    print(Fore.CYAN + Style.BRIGHT +
          "\t\t\t####    ####   ##   ##  ######           ####   ##  ##  ######  ######         " + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT +
          "\t\t\t#      ##  ##  ### ###  ##              ##  ##  ##  ##  ##      ##  ##         " + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT +
          "\t\t\t# ###  ######  ## # ##  ####            ##  ##  ##  ##  ####    #####          " + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT +
          "\t\t\t#  ##  ##  ##  ##   ##  ##              ##  ##   ####   ##      ##  ##         " + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT +
          "\t\t\t####   ##  ##  ##   ##  ######           ####     ##    ######  ##  ##         " + Style.RESET_ALL)
    print(Fore.CYAN+Style.BRIGHT + str("\n\t\t\t\t\t\t\tYOUR SCORE : " +
                                       str(score.value)+"\n")+Style.RESET_ALL)
    quit()
