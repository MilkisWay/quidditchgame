import pygame
import os
import sys
import random
from pygame.locals import *
from basicgame import *
from snitch import *
from quaffle import *

from player import Player
from player import Player_controller

from hunter import Hunter
from hunter import Hunter_controller
from hunter import Hunter_View

from seeker import Seeker
from seeker import Seeker_controller
from seeker import Seeker_View

from ring import Ring
from ring import Ring_controller
from ring import Ring_View

from circle_for_seeker import Circle
from circle_for_seeker import Circle_controller
from circle_for_seeker import Circle_View

from team import Team
from team import Team_controller

class PlayGameState(GameState):
    def __init__(self,game,gameOverState,gameWinState):
        super(PlayGameState,self).__init__(game)
        self.controllers = None
        self.renders =  None

        self.player_controller = None
        self.hunter_controller = None

        self.snitch_controller = None
        self.quaffle_controller = None
        self.gameOverState = gameOverState
        self.gameWinState = gameWinState #dnk  somwhere have to save results to a file
        #and state for records and settings for speed and random
        self.initialise()

    def initialise(self):
        self.ring=Ring(800,500)
        self.ring_render=Ring_View()
        self.ring_controller=Ring_controller(self.ring,self.ring_render)

        self.hunter_computer=Hunter(100,100,1,1,0)
        hunter_computer_render=Hunter_View()
        self.hunter_computer_controller=Hunter_controller(self.hunter_computer,hunter_computer_render)


        self.hunter=Hunter(100,100,1,1,1)
        hunter_render=Hunter_View()
        self.hunter_controller=Hunter_controller(self.hunter,hunter_render)


        self.seeker_2=Seeker(200,200,1,1,0)
        seeker_2_render=Seeker_View()
        self.seeker_2_controller=Seeker_controller(self.seeker_2,seeker_2_render)

        self.seeker=Seeker(600,200,1,1,0)
        seeker_render=Seeker_View()
        self.seeker_controller=Seeker_controller(self.seeker, seeker_render)

        

        self.team_1=Team()
        self.team_1.add_players(self.hunter)
        self.team_1.add_players(self.seeker_2)

        self.team_1_controller=Team_controller(self.team_1)
        self.team_1_controller.add_controller(self.hunter_controller)
        self.team_1_controller.add_controller(self.seeker_controller)

        quaffle = QuaffleModel(100,100,1)
        self.snitch = SnitchModel(random.randint(10,1000),random.randint(10,1900))

        self.snitch_controller = SnitchController(self.snitch)
        #self.quaffle_controller = QuaffleController(quaffle)
        snitch_render = SnitchView(self.snitch_controller)

        self.circle=Circle(700,100,1)
        circle_render=Circle_View()
        self.circle_controller=Circle_controller(self.circle, circle_render)

        #quaffle_render = QuaffleView(self.quaffle_controller)
        self.controllers=[self.snitch_controller,self.circle_controller]
        self.computer_controller=[self.hunter_computer_controller, self.seeker_controller]
        self.renders =[snitch_render,self.hunter_controller,self.hunter_computer_controller, self.seeker_controller,self.circle_controller,self.ring_controller,self.seeker_2_controller]


    def update(self,gameTime):
        self.team_1_controller.update(gameTime)
        self.seeker_2.search(self.circle.pos)

        for i in self.controllers:
            i.update(gameTime)
        for i in self.computer_controller:
            i.computer_update(gameTime)

 

        if self.snitch_controller._ball.endGame()==True:
            if self.snitch_controller._ball.get_who_posses == self.snitch_controller._ball.player_seeker:
                self.game.changeState(self.gameWinState)
            elif self.snitch_controller._ball.get_who_posses == self.snitch_controller._ball.computer_seeker:
                self.game.changeState(self.gameOverState)

    def render(self,surface):
        for i in self.renders:
            i.render(surface)