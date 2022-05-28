import pygame
import os
import sys
import random
from pygame.locals import *
from basicgame import *
from snitch import *
from quaffle import *
from player import *
from hunter import *
from seeker import *
from ring import *
from team import *
from collision import *

class PlayGameState(GameState):
    def __init__(self,game,gameOverState,gameWinState):
        super(PlayGameState,self).__init__(game)
        self.controllers = None
        self.computer_controller = None
        self.snitch_controller = None
        self.quaffle_controller = None
        self.ring_controller=None
        self.hunter_computer_controller=None
        self.hunter_controller=None
        self.seeker_2_controller=None
        self.seeker_controller=None
        self.collision_controller=None
        self.gameOverState = gameOverState
        self.gameWinState = gameWinState #dnk  somwhere have to save results to a file
        #and state for records and settings for speed and random
        self.initialise()

    def initialise(self):
        ring = Ring(100,700)
        quaffle = QuaffleModel(500,100,1)
        snitch = SnitchModel(random.randint(10,1000),random.randint(10,1900))
        hunter_computer=Hunter(100,100,1,1,0,2)
        hunter=Hunter(100,100,1,1,1,1)
        seeker_2=Seeker(200,200,1,1,0,2)
        seeker=Seeker(600,200,1,1,0,1)

        snitch_render = SnitchView()
        quaffle_render = QuaffleView()
        ring_render=Ring_View()
        hunter_computer_render=Hunter_View()
        hunter_render=Hunter_View()
        seeker_2_render=Seeker_View()
        seeker_render=Seeker_View()
        score1=0
        score2=0

        self.snitch_controller = SnitchController(snitch,snitch_render)
        self.quaffle_controller = QuaffleController(quaffle,quaffle_render)
        self.ring_controller=Ring_controller(ring,ring_render)
        self.hunter_computer_controller=Hunter_controller(hunter_computer,hunter_computer_render)
        self.hunter_controller=Hunter_controller(hunter,hunter_render)
        self.seeker_2_controller=Seeker_controller(seeker_2,seeker_2_render)
        self.seeker_controller=Seeker_controller(seeker, seeker_render)
        
        self.collision_controller=CollisionController()

        group=[hunter,seeker_2,hunter_computer]
        team_1=Team(group)
        team_1.add_players(hunter)
        team_1.add_players(seeker_2)
        self.team_1_controller=Team_controller(team_1)

        self.collision_controller.add_hunter(self.hunter_computer_controller)
        self.collision_controller.add_hunter(self.hunter_controller)
        self.collision_controller.add_seeker(self.seeker_2_controller)
        self.collision_controller.add_seeker(self.seeker_controller)
        #self.collision_controller.add_score_for_team(score1)
        #self.collision_controller.add_score_for_team(score2)
        self.collision_controller.add_quaffle(self.quaffle_controller)
        self.collision_controller.add_snitch(self.snitch_controller)
        self.collision_controller.add_ring(self.ring_controller)

        self.controllers=[self.snitch_controller,self.quaffle_controller,self.hunter_controller,self.ring_controller]
        self.computer_controller=[self.hunter_computer_controller, self.seeker_controller, self.seeker_2_controller]

    #def seeker_funstion(seeker,circle,gameTime,ring):#not here
        #if self.seeker_2.quaffle==None:
            #self.seeker_2.search(circle,gameTime,ring)

    def update(self,gameTime):

        for i in self.controllers:
            i.update(gameTime)
        for i in self.computer_controller:
            i.computer_update(gameTime)
        self.collision_controller.update(gameTime)
        #if self.snitch_controller._ball.endGame()==True:
            #if self.snitch_controller._ball.get_who_posses == self.snitch_controller._ball.player_seeker:
                #self.game.changeState(self.gameWinState)
            #elif self.snitch_controller._ball.get_who_posses == self.snitch_controller._ball.computer_seeker:
                #self.game.changeState(self.gameOverState)
    
    def render(self,surface):
        for i in self.controllers:
            i.render(surface)
        for i in self.computer_controller:
            i.render(surface)