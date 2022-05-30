import pygame
import os
import sys
from pygame.locals import *
from basicgame import *


class GameWinState(GameState):
    def __init__(self,game):
        super(GameWinState,self).__init__(game)
        self.font = pygame.font.Font('MagicSchoolOne.ttf',80)
        self.mainMenuState = None
        self.image = pygame.image.load('MenuBack.jpg')
        self.height=500
        self.width=900

    def setMainMenu(self,state):
        self.mainMenuState = state
    def render(self,surface):
        surface.blit(self.image,(0,0))
        surface.blit(self.font.render("You won!",True,(237, 213, 79)),(self.width,self.height))
    
    def update(self, gameTime):
        keys = pygame.key.get_pressed()
        if keys[QUIT]:
            self.game.changeState(None)
