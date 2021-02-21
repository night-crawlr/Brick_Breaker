import os
from screen import *
from constants import *
from paddle import *
from input import *
from ball import *
from background import *
import time
from Bricks import *
from power import *

os.system('clear')

whole_screen = Screen(screen_ht, screen_wd)
score = Score()
lives = Lives()
Time = Time()
paddle = Paddle()
ball = Ball(paddle.col_start)
get = Get()
background = Background()
bricks = Bricks()
bricks.generate(total_bricks)
allPowers = Powers()

start_time = time.time()
render_time = time.time()

pause = 0
forward = 0


def toggle_pause(pause):
    return (1 - pause)


def check_collisions():
    # side wall collisions are done

    # paddle collison with sides
    if(paddle.col_start <= game_wd[0]):
        paddle.col_start = game_wd[0]
    if((paddle.col_start + len(paddle.paddle) - 1) >= (game_wd[1] - 1)):
        paddle.col_start = game_wd[1]-len(paddle.paddle)


def display_game(iter, lives, paddle):
    flag = 1
    for brick in bricks.bricks:
        if(brick.ret_is_broken() == 0 and brick.ret_type() > 0):
            flag = 0
    if(flag == 1):
        over(score)
    background.show(whole_screen.screen)
    score.show(whole_screen.screen)
    lives.show(whole_screen.screen)
    Time.show(whole_screen.screen, round(time.time() - start_time))
    paddle.show(whole_screen.screen)
    ball.show(whole_screen.screen, lives, paddle,
              bricks.bricks, score,  allPowers)
    bricks.show(whole_screen.screen)
    allPowers.show(whole_screen.screen, paddle, ball)
    check_collisions()
    whole_screen.display_screen()

    print("\033[0:0H")  # reposition the cursor


def handle_input(pause, forward):
    ch = input_to(get, 0.1)

    if(ch == 'd'):
        paddle.clear(whole_screen.screen)
        paddle.col_start += 2
        check_collisions()
        if(ball.ret_is_started() == 0):
            ball.clear(whole_screen.screen)
            ball.upd_col(ball.ret_col() + 2)
        else:
            if(ball.grabed == 1):
                ball.clear(whole_screen.screen)
                ball.upd_col(ball.ret_col() + 2)
    if(ch == 'a'):
        paddle.clear(whole_screen.screen)
        paddle.col_start -= 2
        check_collisions()
        if(ball.ret_is_started() == 0):
            ball.clear(whole_screen.screen)
            ball.upd_col(ball.ret_col() - 2)
        else:
            if(ball.grabed == 1):
                ball.clear(whole_screen.screen)
                ball.upd_col(ball.ret_col() - 2)
    if(ch == 'p'):
        return(toggle_pause(pause), forward)
    if(ch == 'f'):
        return (0, 1)
    if(ch == " "):
        if(ball.ret_is_started() == 0):
            ball.start()
        else:
            if(ball.grabed == 1):
                ball.resume(paddle)

    if(ch == 'q'):
        over(score)
    return pause, forward


iter = 0
while(True):
    iter += 1
    pause, forward = handle_input(pause, forward)
    if(forward == 1):
        forward = 0
        pause = 1
    while(pause):
        pause, forward = handle_input(pause, forward)
    if(time.time() - render_time >= 0.1):
        display_game(iter, lives, paddle)
        render_time = time.time()
    # time.sleep(0.1)
    # if(ball.is_started == 0):
    #     ball.start()
