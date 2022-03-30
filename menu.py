import pygame
import os
import sys
from pygame.locals import *
from basicgame import *

class MainMenuState(GameState):
    def __init__(self,game):
        super(MainMenuState,self).__init__(game)
        self.playGameState == None
        self.font = pygame.font.SysFont("rockwellextra",12,12)
        self.index = 0
        self.inputTick = 0
        self.menuItems = ['Start Game','Records','Mode','Quit']
