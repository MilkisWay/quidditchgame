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
        self.index = 0 #currently selected item is stored in 'index'
        self.inputTick = 0
        self.menuItems = ['Start Game','Records','Mode','Quit']
    def setPlayState(self,state):
        self.playGameState = state
    def update(self, gameTime): #here should write work with keys to choose menu items
        keys = pygame.key.pet_pressed()
        if ((keys[K_w] or keys[K_s]) and self.inputTick = 0):
            self.inputTick = 250
            if (keys[K_w]):
                self.index -= 1 #index controlls what is happening
                if (self.index<0):

    def draw(self,surface): #here senarios, when people click
        pass
        
