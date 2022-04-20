import pygame
import os
import sys
import random
from pygame.locals import *
from basicgame import *
from snitch import *
from quaffle import *

class PlayGameState(GameState):
    def __init__(self,game,gameOverState,gameWinState):
        super(PlayGameState,self).__init__(game)
        self.controllers = None
        self.renders =  None
        self.player_controller = None
        self.snitch_controller = None
        self.quaffle_controller = None
        self.gameOverState = gameOverState
        self.gameWinState = gameWinState #dnk  somwhere have to save results to a file
        #and state for records and settings for speed and random
        self.initialise()
    def initialise(self):
        quaffle = QuaffleModel(100,100,1)
        snitch = SnitchModel(random.randint(10,1000),random.randint(10,1900))
        self.snitch_controller = SnitchController(snitch)
        self.quaffle_controller = QuaffleController(quaffle)
        snitch_render = SnitchView(self.snitch_controller)
        quaffle_render = QuaffleView(self.quaffle_controller)
        self.controllers=[self.snitch_controller,self.quaffle_controller]
        self.renders =[snitch_render,quaffle_render]
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