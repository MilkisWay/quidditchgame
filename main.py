import pygame
import os
import sys
from pygame.locals import *
from basicgame import *
from interstitial import *
from menu import MainMenuState

quidditch = BasicGame("Harry Potter")
mainMenuState = MainMenuState(quidditch)


quidditch.run(mainMenuState)