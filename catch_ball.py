import pygame
from ball import Ball
from setting import Settings
from unit import Unit
from setting import Setting


def catch_ball():
    set=Setting()
    ball = Ball(screen=screen, sets=sets)
    unit= Unit(screen=screen, sets=sets)

    while True:
        if set.finish == False :
            ball.drop_ball(sets=sets)    
            f.update_ball(ball=ball, bowl=bowl, sets=sets)





