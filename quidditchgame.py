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
    def __init__(self,game):
        super(PlayGameState,self).__init__(game)
        self.game=game
        self.controllers = None
        self.computer_controller = None
        self.snitch_controller = None
        self.quaffle_controller = None
        self.ring_controller=None
        self.hunter_computer_controller=None
        self.hunter_controller=None
        self.seeker_controller_2=None
        self.seeker_controller=None
        self.collision_controller=None
        self.team_1_controller=None
        self.setup=game.setup
        self.gameWinState = None
        self.gameOverState = None
        #and state for records and settings for speed and random
        self.initialise()

    
    def setgameWin(self,state):
        self.gameWinState = state

    def setgameOverState(self,state):
        self.gameOverState = state
    
    def initialise(self):
        ring = Ring(10,700)
        ring2 = Ring(1380,700)
        quaffle = QuaffleModel(1000,100,1)
        snitch = SnitchModel(random.randint(10,1000),random.randint(10,1900))
        hunter_computer=Hunter(100,100,1,1,1,self.game,"Team1_hunter.png")
        hunter_computer_2=Hunter(200,100,1,1,2,self.game,"Team2_hunter.png")
        hunter_computer_3=Hunter(200,100,1,1,2,self.game,"Team2_hunter.png")
        hunter=Hunter(500,100,1,1,1,self.game,"Team1_hunter.png")
        seeker_2=Seeker(200,200,1,1,1,self.game,"Team1_Seeker.png")
        seeker=Seeker(600,200,1,1,2,self.game,"Team2_Seeker.png")

        snitch_render = SnitchView()
        quaffle_render = QuaffleView()
        ring_render=Ring_View()
        ring_render2=Ring_View()
        hunter_computer_render=Hunter_View("Team1_hunter.png")
        hunter_computer_render_2=Hunter_View("Team2_hunter.png")
        hunter_computer_render_3=Hunter_View("Team2_hunter.png")
        hunter_render=Hunter_View("Team1_hunter.png")
        seeker_2_render=Seeker_View("Team1_Seeker.png")
        seeker_render=Seeker_View("Team2_Seeker.png")
        score1=0
        score2=0

        self.snitch_controller = SnitchController(snitch,snitch_render)
        self.quaffle_controller = QuaffleController(quaffle,quaffle_render)
        self.ring_controller=Ring_controller(ring,ring_render)
        self.ring_controller2=Ring_controller(ring2,ring_render2)
        self.hunter_computer_controller=Hunter_controller(hunter_computer,hunter_computer_render)
        self.hunter_computer_controller_2=Hunter_controller(hunter_computer_2,hunter_computer_render_2)
        self.hunter_computer_controller_3=Hunter_controller(hunter_computer_3,hunter_computer_render_3)
        self.hunter_controller=Hunter_controller(hunter,hunter_render)
        self.seeker_controller_2=Seeker_controller(seeker_2,seeker_2_render)
        self.seeker_controller=Seeker_controller(seeker, seeker_render)
        
        self.collision_controller=CollisionController()

        controlers_1=[self.hunter_controller,self.seeker_controller_2,self.hunter_computer_controller]
        group=[hunter,seeker_2,hunter_computer]
        team_1=Team(group)
        self.team_1_controller=Team_controller(team_1, controlers_1)
        team_1.add_activity(hunter)
        team_1.add_passivity_player(seeker_2)


        controlers_2=[]
        group_2=[seeker,hunter_computer_2,hunter_computer_3]
        team_2=Team(group_2)
        self.team_2_controller=Team_controller(team_2,controlers_2)


        self.collision_controller.add_hunter(self.hunter_computer_controller)
        self.collision_controller.add_hunter(self.hunter_controller)
        self.collision_controller.add_seeker(self.seeker_controller_2)
        self.collision_controller.add_hunter(self.hunter_computer_controller_2)
        self.collision_controller.add_hunter(self.hunter_computer_controller_3)
        self.collision_controller.add_seeker(self.seeker_controller)
        self.collision_controller.add_score_for_team(score1)
        #self.collision_controller.add_score_for_team(score2)
        self.collision_controller.add_quaffle(self.quaffle_controller)
        self.collision_controller.add_snitch(self.snitch_controller)
        self.collision_controller.add_ring(self.ring_controller)
        self.collision_controller.add_ring(self.ring_controller2)
        self.collision_controller.add_basic_setup(self.game)

        self.controllers=[self.snitch_controller,self.team_1_controller]

        #self.computer_controller=[self.hunter_computer_controller, self.seeker_controller, self.hunter_computer_controller_2, self.hunter_computer_controller_3]

        self.renders=[self.snitch_controller,self.quaffle_controller,self.seeker_controller_2,self.hunter_controller,self.ring_controller2, self.ring_controller]

        self.renders_computer=[self.hunter_computer_controller, self.hunter_computer_controller_2, self.hunter_computer_controller_3,self.seeker_controller]
    #def seeker_funstion(seeker,circle,gameTime,ring):#not here
        #if self.seeker_2.quaffle==None:
            #self.seeker_2.search(circle,gameTime,ring)

    def update(self,gameTime):
        
        for i in self.controllers:
            i.update(gameTime)
            self.seeker_controller.player.search(self.snitch_controller.ball, self.ring_controller.ring)
            self.hunter_computer_controller_2.player.search(self.quaffle_controller.ball,self.ring_controller.ring)
            self.hunter_computer_controller_3.player.computer_update_3(gameTime)
            #self.hunter_computer_controller_2.player.computer_update_3(gameTime)
            self.hunter_computer_controller.player.computer_update_3(gameTime)
   
        

        self.collision_controller.update(gameTime)

        if self.snitch_controller.ball.possession==True:
            screen = pygame.display.set_mode((1920,1080))
            screen_b=pygame.image.load('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Photos/Background1.jpg')
            screen.blit(screen_b,(0,0))
            f1 = pygame.font.Font(None, 72)
            if self.snitch_controller.ball.who_possess == 1:
                self.game.changeState(self.gameWinState)
            elif self.snitch_controller.ball.who_possess == 2:
                self.game.changeState(self.gameOverState)
    
    def render(self,surface):
        self.collision_controller.render(surface)
        for i in self.renders:
            i.render(surface)
        for i in self.renders_computer:
            i.render_computer(surface)
         