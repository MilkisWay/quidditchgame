import pygame
import os
import sys
from pygame.locals import *
from basicgame import *

class MainMenuState(GameState):
    def __init__(self,game):
        super(MainMenuState,self).__init__(game)
        self.font = pygame.font.Font('MagicSchoolOne.ttf',80)
        self.__playGameState = None
        self.index = 0 #currently selected item is stored in 'index'
        self.image = pygame.image.load('MenuBack.jpg')
        self.image1 = pygame.image.load('menuname.png')
        self.inputTick = 0
        self.menu_width=1920
        self.menu_height=1080
        self.menuItems = ['Start Game','Records','Settings','Quit']
        #self._mode=1
    #def get_Game_Mode(self):
        #return self._mode
    #def set_Game_Mode(self,x:int):
        #self._mode=x

    def setPlayState(self,state):
        self.__playGameState = state

    def update(self, gameTime):
        keys = pygame.key.get_pressed()
        if ((keys[K_w] or keys[K_s]) and self.inputTick == 0):
            self.inputTick = 250
            if keys[K_w]:
                self.index = self.index - 1 #index controlls what is happening
                if (self.index<0):
                    self.index = len(self.menuItems) - 1
            elif keys[K_s]:
                 self.index= self.index + 1
                 if self.index == len(self.menuItems):
                     self.index=0
        elif self.inputTick>0: #scrolling control
            self.inputTick -= gameTime
        if self.inputTick<0:
            self.inputTick=0
        if (keys[K_RETURN]):
            if self.index == 3:
                self.game.changeState(None)#Exit the game
            elif self.index == 2:
                self.game.changeState(None)#add Settings state
            elif self.index == 1:
                self.game.changeState(None)#add state to read reacords
            elif self.index == 0:
                self.game.changeState(self.__playGameState)#Start the Game
    def render(self,surface): #here senarios, when people click
        surface.blit(self.image,(0,0))
        surface.blit(self.image1,(500,100))
        count=0
        y=self.menu_height//2+50
        for item in self.menuItems:
            itemText = ' '
            if count == self.index:
                itemText = '>>'
            itemText += item
            surface.blit(self.font.render(itemText,True,(249,214,46)),(500,y))
            y -= 100
            count += 1
       
