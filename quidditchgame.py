import pygame
import os
import sys
from pygame.locals import *
from basicgame import *
from snitch import *
import random
#import everything in here


class PlayGameState(GameState):
    def __init__(self,game,gameOverState,gameWinState):
        super(PlayGameState,self).__init__(game)
        self.controllers = None
        self.renders =  None
        self.player_controller = None
        self.snitch_controller = None
        self.gameOverState = gameOverState
        self.gameWinState = gameWinState#dnk but somwhere have to save results to a file
        #and state for records and settings for speed and random
        self.initialise()
    def onEnter(self,previousState):
        pass #here comes player_controller
    def initialise(self):
        snitch = SnitchModel(random.randint(10,1000),random.randint(10,1900))
        self.snitch_controller = SnitchController(snitch)
        snitch_render = SnitchView(self.snitch_controller)
        self.controllers=[self.snitch_controller]
        self.renders =[snitch_render]
    def update(self,gameTime):
        for i in self.controllers:
            i.update(gameTime)
        if self.snitch_controller._ball.endGame()==True:
            if self.snitch_controller._ball.get_who_posses == self.snitch_controller._ball.player_seeker:
                self.game.changeState(self.gameWinState)
            elif self.snitch_controller._ball.get_who_posses == self.snitch_controller._ball.computer_seeker:
                self.game.changeState(self.gameOverState)
    def render(self,surface):
        for i in self.renders:
            i.render(surface)