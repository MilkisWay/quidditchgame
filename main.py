import pygame
import os
import sys
from pygame.locals import *
from setup import Setup
from basicgame import *
from interstitial import *
from menu import MainMenuState
from quidditchgame import PlayGameState
from settings import SettingsState

basic = Setup()
quidditch = BasicGame("Harry Potter",basic)
mainMenuState = MainMenuState(quidditch)
gameOverState = InterstitialState(quidditch, 'GAME OVER!', 5000, mainMenuState)
gameWinState = InterstitialState(quidditch, 'CONGRATULATIONS!\n YOU WON!', 5000, mainMenuState)
playGameState= PlayGameState(quidditch,gameOverState,gameWinState)
getReadyState = InterstitialState(quidditch,'Get Ready!',2000, playGameState)
settingsState = SettingsState(quidditch)
mainMenuState.setPlayState(getReadyState)
mainMenuState.setSettingsState(settingsState)
settingsState.setMainMenu(mainMenuState)
quidditch.run(mainMenuState)