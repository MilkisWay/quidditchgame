import pygame
import os
import sys
from pygame.locals import *
from basicgame import *

class InterstitialState(GameState):
    def __init__(self, game, msg,waitTimeMs, nextState):
        super(InterstitialState,self).__init__(game)
        self.nextState = nextState
        self.font = pygame.font.Font('ParryHotter.ttf',100)
        self.message = msg
        self.waitTimer = waitTimeMs

    def update(self,gameTime):
        self.waitTimer -= gameTime
        if (self.waitTimer < 0):
            self.game.changeState(self.nextState)

    def render(self, surface):
        surface.blit(self.font.render(self.message,True,(238, 183, 0)),(680,240))