import pygame
import os
import sys
from pygame.locals import *
from menu import *

class Mode(object):
    def __init__(self):
        self.mode = 1
        self.mode_A=self.mode*2
        self.mode_B=self.mode*4