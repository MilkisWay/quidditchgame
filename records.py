import pygame
import os
import sys
from pygame.locals import *
from basicgame import *

class RecordsState(GameState):
    def __init__(self,game):
        super(RecordsState,self).__init__(game)
        self.font = pygame.font.Font('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Fonts/MagicSchoolOne.ttf',80)
        self.mainMenuState = None
        self.index = 0
        self.image = pygame.image.load('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Photos/MenuBack.jpg')
        self.inputTick = 0
        self.oneItem = ['Back']

    def setMainMenu(self,state):
        self.mainMenuState = state

    def update(self, gameTime):
        keys = pygame.key.get_pressed()
        if (keys[K_RETURN]):
            self.game.changeState(self.mainMenuState)
    def render(self,surface):
        surface.blit(self.image,(0,0))
        itemText = ' '
        itemText+=self.oneItem
        surface.blit(self.font.render(itemText,True,(273,213.79)),(500,y))
