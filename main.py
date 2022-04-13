import pygame
import os
import sys
from pygame.locals import *
from basicgame import *
from interstitial import *
from menu import MainMenuState
from quidditchgame import PlayGameState

quidditch = BasicGame("Harry Potter")
mainMenuState = MainMenuState(quidditch)
gameOverState = InterstitialState(quidditch, 'GAME OVER!', 5000, mainMenuState)
gameWinState = InterstitialState(quidditch, 'CONGRATULATIONS!\n YOU WON!', 5000, mainMenuState)
playGameState= PlayGameState(quidditch,gameOverState,gameWinState)
getReadyState = InterstitialState(quidditch,'Get Ready!',20, playGameState)
mainMenuState.setPlayState(getReadyState)
quidditch.run(mainMenuState)