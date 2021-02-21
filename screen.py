from constants import *
from colorama import init, Fore, Back, Style
init()
# Screen contains whole game area including left of display


class Screen:
    def __init__(this, r, c):
        this.r = r
        this.c = c
        this.screen = []
        # initialize screen with spaces
        for i in range(this.r):
            this.screen.append([])
            for j in range(this.c):
                this.screen[i].append(' ')

    # def display_screen(this):
    #     for i in range(this.r):
    #         for j in range(this.c):
    #             tobeprinted = this.screen[i][j]
    #             print(tobeprinted, end='')

    def display_screen(this):
        print()
        for i in range(this.r):
            for j in range(this.c):
                tobeprinted = this.screen[i][j]
                if(tobeprinted == 1):
                    print(Back.RED + ' ' + Style.RESET_ALL, end='')
                elif(tobeprinted == 2):
                    print(Back.BLUE + ' ' + Style.RESET_ALL, end='')
                elif(tobeprinted == 3):
                    print(Back.YELLOW + ' ' + Style.RESET_ALL, end='')
                elif(tobeprinted == 0):
                    print(Back.WHITE + ' ' + Style.RESET_ALL, end='')
                elif(tobeprinted == '|' or tobeprinted == '_' or (i == game_ht[0] and j == game_wd[1]-1) or (i == game_ht[1] and j == game_wd[0]) or (i == game_ht[1] and j == game_wd[1]-1) or (i == game_ht[0] and j == game_wd[0])):
                    print(Back.GREEN + ' ' + Style.RESET_ALL, end='')
                elif(tobeprinted == '{' or tobeprinted == '}'):
                    print(Back.MAGENTA + ' '+Style.RESET_ALL, end='')
                else:
                    print(tobeprinted, end='')


class Header:
    def __init__(this):
        this.label = 'Header'
        this.value = 0
        this.sy = 10
        this.sx = 10

    def show(this, screen):
        for i, val in enumerate(this.label):
            screen[this.sx][this.sy+i] = val
        for i, val in enumerate(str(this.value)):
            screen[this.sx][this.sy+len(str(this.label)) + i] = val


class Score(Header):
    def __init__(this):
        Header.__init__(this)
        this.label = 'SCORE = '


class Lives(Header):
    def __init__(this):
        Header.__init__(this)
        this.label = 'LIVES = '
        this.value = 9
        this.sx = 20

    def dec_life(this):
        this.value -= 1


class Time(Header):
    def __init__(this):
        Header.__init__(this)
        this.label = 'TIME = '
        this.sx = 30

    def show(this, screen, time):
        for i, val in enumerate(str(this.label)):
            screen[this.sx][this.sy+i] = val
        for i, val in enumerate(str(time)):
            screen[this.sx][this.sy+len(str(this.label)) + i] = val
