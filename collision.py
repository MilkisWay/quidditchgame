import pygame
import os
import sys
from pygame.locals import *
from interstitial import *
#add player, ball and so on

class CollisionController(object):
    def __init__(self,game,player,ball,playState):
        self.ball= ball
        self.player = player
        self.game = game
        self.playState = playState
        #self.sound add winning sound
    def update(self, gameTime):
        pass

