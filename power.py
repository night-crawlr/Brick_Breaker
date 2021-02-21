
import random
from constants import *
powerups = ["EP", "SP", "BM", "FB", "TB", "PG"]


class Powers:
    def __init__(this):
        this.powers = []

    def generate_powerup(this, r, c):
        selcted_power = random.choice(
            [EP(r, c), SP(r, c), FB(r, c), TB(r, c), PG(r, c)])
        #selcted_power = random.choice([PG(r, c)])
        this.powers.append(selcted_power)

    def remove(this, i):
        this.powers.pop(i)

    def collison_paddle(this, power, paddle, ball):
        flag = 0
        if(power.row == paddle_row):
            for i in range(len(paddle.paddle)):
                if(power.col == paddle.col_start + i):
                    flag = 1
                    if(power.type == "EP"):
                        paddle.expand()
                    if(power.type == "SP"):
                        paddle.contract()
                    if(power.type == "FB"):
                        ball.speedup()
                    if(power.type == "TB"):
                        ball.superball()
                    if(power.type == "PG"):
                        paddle.grab()
        return flag

    def show(this, screen, paddle, ball):
        dummy = []
        for v in this.powers:
            dummy.append(v)
        for i, power in enumerate(dummy):
            screen[power.row - power.row_vel][power.col] = ' '
            screen[power.row - power.row_vel][power.col + 1] = ' '
            if(this.collison_paddle(power, paddle, ball)):
                this.remove(i)
                continue
            if(power.row >= game_ht[1]):
                this.remove(i)
                continue
            screen[power.row][power.col] = power.type[0]
            screen[power.row][power.col+1] = power.type[1]
            power.row += power.row_vel


class Power:
    def __init__(this):
        this.row = 0
        this.col = 0
        this.type = 0
        this.row_vel = 1


class EP(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "EP"


class SP(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "SP"


class FB(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "FB"


class TB(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "TB"


class PG(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "PG"
