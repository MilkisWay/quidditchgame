import pygame
import os
import sys
from pygame.locals import *
from basicgame import *

class SettingsState(GameState):
    def __init__(self,game):
        super(SettingsState,self).__init__(game)
        self.font = pygame.font.Font('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Fonts/MagicSchoolOne.ttf',80)
        self.index = 0
        self.mode = 1
        self.inputTick = 0
        self.background = pygame.image.load("Add")
        self.modeItems = ['Easy','Medium','Hard','Death']

    def update(self, gameTime):
        keys = pygame.key.get_pressed()
        if ((keys[K_w] or keys[K_s]) and self.inputTick == 0):
            self.inputTick = 250
            if keys[K_w]:
                self.index = self.index - 1
                if (self.index<0):
                    self.index = len(self.modeItems) - 1
            elif keys[K_s]:
                 self.index= self.index + 1
                 if self.index == len(self.modeItems):
                     self.index=0
        elif self.inputTick>0:
            self.inputTick -= gameTime
        if self.inputTick<0:
            self.inputTick=0
        if (keys[K_RETURN]):
            if self.index == 3:
                self.mode = 1
            elif self.index == 2:
                self.mode = 2
            elif self.index == 1:
                self.mode = 3
            elif self.index == 1:
                self.mode = 4

    def render():
        pass