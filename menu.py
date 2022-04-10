import pygame
import os
import sys
from pygame.locals import *
from basicgame import *

class MainMenuState(GameState):
    def __init__(self,game):
        super(MainMenuState,self).__init__(game)
        self.playGameState == None
        self.font = pygame.font.Font('MagicSchoolOne.ttf',48)
        self.index = 0 #currently selected item is stored in 'index'
        self.image =pygame.image.load('wp7698391-harry-potter-aesthetic-pc-wallpapers.jpg')
        self.inputTick = 0
        self.menu_width=1280
        self.menu_height=720
        self.menuItems = ['Start Game','Records','Settings','Quit']
        self._mode=1
    def get_Game_Mode(self):
        return self._mode
    def set_Game_Mode(self,x:int):
        self._mode=x
    def setPlayState(self,state):
        self.playGameState = state
    def update(self, gameTime):
        keys = pygame.key.pet_pressed()
        if ((keys[K_w] or keys[K_s]) and self.inputTick == 0):
            self.inputTick = 250
            if keys[K_w]:
                self.index -= 1 #index controlls what is happening
                if (self.index<0):
                    self.index = len(self.menuItems) -1
            elif keys[K_s]:
                 self.index+=1
                 if self.index == len(self.menuItems):
                     self.index=0
        elif self.inputTick>0: #scrolling control
            self.inputTick -= gameTime
        if self.inputTick<0:
            self.inputTick=0
    def render(self,surface): #here senarios, when people click
        surface.blit(self.image,(self.menu_width,self.menu_height))
        surface.blit(self.font.render('Quidditch',True,(249,214,46),(self.menu_width//2,self.menu_height//2+150)))
        count=0
        y=self.menu_height//2+50
        for item in self.menuItems:
            itemText = ' '
            if count == self.index:
                itemText = '>>'
            itemText += item
            surface.blit(self.font.render(itemText,True,(249,214,46),(self.menu_width//2,y)))
            y -= 100
            count += 1
       
