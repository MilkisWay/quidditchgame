import pygame
import os
import sys
from pygame.locals import *
from basicgame import *

class SettingsState(GameState):
    def __init__(self,game):
        super(SettingsState,self).__init__(game)
        self.font = pygame.font.Font('MagicSchoolOne.ttf',80)
        self.mainMenuState = None
        self.index = 0
        self.image = pygame.image.load('MenuBack.jpg')
        self.mode = 1
        self.inputTick = 0
        self.modeItems = ['Easy','Medium','Hard','Death']

    def setMainMenu(self,state):
        self.mainMenuState = state

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
                self.game.changeState(self.mainMenuState)
            elif self.index == 2:
                self.mode = 2
                self.game.changeState(self.mainMenuState)
            elif self.index == 1:
                self.mode = 3
                self.game.changeState(self.mainMenuState)
            elif self.index == 0:
                self.mode = 4
                self.game.changeState(self.mainMenuState)

    def render(self,surface):
        surface.blit(self.image,(0,0))
        count=0
        y=1080//2+50
        for item in self.modeItems:
            itemText = ' '
            if count == self.index:
                itemText = '>'
            itemText += item
            surface.blit(self.font.render(itemText,True,(237, 213, 79)),(500,y))
            y -= 100
            count += 1 