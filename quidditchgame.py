import pygame
import os
import sys
from pygame.locals import *
from basicgame import *
#import everything in here


class PlayGameState(Gamestate):
    def __init__(self,game,gameOverState,gameWinState):
        super(PlayGameState,self).__init__(game)
        self.controllers = None
        self.renders =  None
        self.player_controller = None
        self.ball_controller = None
        self.gameOverState = gameOverState
        self.gameWinState = gameWinState
        self.initialise()
    def onEnter(self,previousState):
        pass #here comes player_controller
    def initialise(self):
        pass #here call all controllers
    def update(self,gameTime):
        for i in self.controllers:
            i.update(gameTime)
        #if (another team got snitch):
            #self.game.changeState(self.gameOverState)
        #elif (our team got snitch):
            #self.game.changeState(self.gameWinState)
    def draw(self,surface):
        for i in sel.renders:
            i.render(surface)