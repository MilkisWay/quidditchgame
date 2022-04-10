import pygame
import os
import sys
from pygame.locals import *
from menu import *

class Mode(object):
    def __init__(self,gameMode:MainMenuState):
        self.__mode = gameMode.get_Game_Mode()
    def get_Game_Mode(self):
        return self.__mode