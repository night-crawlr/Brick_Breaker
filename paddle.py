import random
from constants import *


class Paddle:
    def __init__(this):
        this.paddle_size = 14
        this.paddle = ['{', '{', '{', '{', '{', '{', '{',
                       '{', '{', '{', '{', '{', '{', '{']  # 11 sized  40,0 to 40,13
        this.vels = [-6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6]
        this.row = paddle_row
        this.col_start = random.randint(game_wd[0], game_wd[1]-20)
        this.power = 0  # can be 1,2,3
        this.power_timer = 0

    def create_vels(this, len):
        vels = []
        for i in range(len):
            j = i+1
            vels.append(j - (len//2))
        return vels

    def expand(this, flag=0):
        if(this.paddle_size == paddle_size):
            this.paddle_size = Ex_paddle_size
            this.paddle = ['}' for i in range(this.paddle_size)]
        elif(this.paddle_size == small_paddle_size):
            this.paddle_size = paddle_size
            this.paddle = ['{' for i in range(this.paddle_size)]
        this.vels = this.create_vels(this.paddle_size)
        if(flag == 0):
            this.power = 1
            this.power_timer = time.time()
        else:
            this.power = 0

    def contract(this, flag=0):
        if(this.paddle_size == paddle_size):
            this.paddle_size = small_paddle_size
            this.paddle = ['}' for i in range(this.paddle_size)]
        elif(this.paddle_size == Ex_paddle_size):
            this.paddle_size = paddle_size
            this.paddle = ['{' for i in range(this.paddle_size)]
        this.vels = this.create_vels(this.paddle_size)
        if(flag == 0):
            this.power = 2
            this.power_timer = time.time()
        else:
            this.power = 0

    def grab(this):
        this.power = 3
        this.power_timer = time.time()

    def reset(this, screen):
        this.clear(screen)
        this.paddle_size = paddle_size
        this.paddle = ['{' for i in range(this.paddle_size)]
        this.vels = this.create_vels(this.paddle_size)
        this.col_start = random.randint(game_wd[0], game_wd[1]-20)
        this.power = 0
        this.power_timer = 0

    def clear(this, screen):
        # for j in range(len(this.paddle)):
        #     screen[this.row][this.col_start + j] = ' '
        for j in range(game_wd[0]+1, game_wd[1]-2):
            screen[this.row][j] = ' '

    def show(this, screen):
        this.clear(screen)
        if(time.time() - this.power_timer >= timer_time and this.power != 0):
            if(this.power == 1):
                this.contract(flag=1)
            if(this.power == 2):
                this.expand(flag=1)

        for j in range(len(this.paddle)):
            screen[this.row][this.col_start + j] = this.paddle[j]
