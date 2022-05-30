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
from gameover import *
from gamewin import *

basic = Setup()
quidditch = BasicGame("Harry Potter",basic)
mainMenuState = MainMenuState(quidditch)
gameOverState = GameOverState(quidditch)
gameWinState = GameWinState(quidditch)
playGameState= PlayGameState(quidditch)
getReadyState = InterstitialState(quidditch,'Get Ready!',2000, playGameState)
settingsState = SettingsState(quidditch)
mainMenuState.setPlayState(getReadyState)
mainMenuState.setSettingsState(settingsState)
settingsState.setMainMenu(mainMenuState)
playGameState.setgameOverState(gameOverState)
playGameState.setgameWin(gameWinState)
quidditch.run(mainMenuState)