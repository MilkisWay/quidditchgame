import pygame
import os
import sys
from pygame.locals import *
from setup import *

class GameState(object):
    def __init__(self, game):
        self.game=game
    def onEnter(self,previousState):
        pass
    def onExit(self):
        pass
    def update(self, gameTime):
        pass
    def draw(self, surface):
        pass

class BasicGame(object):
    def __init__(self, gameName,setup):
        pygame.init()
        pygame.display.set_caption(gameName);
        self.setup=setup
        self.screen_width=self.setup.screen_width
        self.screen_height=self.setup.screen_height
        self.fpsClock = pygame.time.Clock()
        self.mainwindow = pygame.display.set_mode(( self.screen_width,self.screen_height),HWSURFACE)
        self.background = pygame.image.load('Background1.jpg')
        self.currentState = None

    def changeState(self,newState):
        if self.currentState!=None:
            self.currentState.onExit()

        if newState == None:
            pygame.quit()
            sys.exit()

        oldState = self.currentState
        self.currentState = newState
        newState.onEnter(oldState)

    def run(self,initialState):

        self.changeState(initialState)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            gameTime = self.fpsClock.get_time()

            if self.currentState!=None:
                self.currentState.update(gameTime)

            self.mainwindow.blit(self.background,(0,0))

            if self.currentState!=None:
                 self.currentState.render(self.mainwindow)

            pygame.display.update()
            self.fpsClock.tick(40)


            