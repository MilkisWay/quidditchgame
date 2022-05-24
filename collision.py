import pygame
import os
import sys
from pygame.locals import *
from interstitial import *
#add player, ball and so on

class CollisionController(object):
    def __init__(self):
        self._hunters=[]
        self.quaffle=None
        self._seekers=[]
        self.snitch=None
        self.types=[1,2]
        self.rings=[]
        self._collision_detected = False
        self.score=[]

    def add_score_for_team(self,score1):
        self.score.append(score1)

    def add_hunter(self,object1):
        self._hunters.append(object1)

    def add_seeker(self,object1):
        self._seekers.append(object1)

    def add_quaffle(self,object1):
        self.quaffle=object1

    def add_ring(self,object1):
        self.rings.append(object1)

    def add_snitch(self,object1):
        self.snitch=object1

    def check(self,object1):
        if object1.get_Coord_x()>=1920:
            object1.set_Coord_x(object1.get_Coord_x()-10)
        elif object1.get_Coord_x()<=0:
            object1.set_Coord_x(object1.get_Coord_x()+10)
        if object1.get_Coord_y()>=1080:
              object1.set_Coord_y(object1.get_Coord_y()-10)
        elif object1.get_Coord_y()<=0:
                object1.set_Coord_y(object1.get_Coord_y()+10)

    def check_if_on_screen(self):
        for i in self._hunters:
            self.check(i.player)
        for i in self._seekers:
            self.check(i.player)
        self.check(self.quaffle.ball)
        self.check(self.snitch.ball)

    def check_quaffle(self):
        if self.quaffle.ball._possession==False:
            if self.quaffle.ball.quaffle_holder_type!=None:
                for b in self.types:
                    if self.quaffle.ball.quaffle_holder_type==b:
                        for i in self._hunters:
                            if ((i.player.get_Coord_x()-self.quaffle.ball.get_Coord_x())**2+(i.player.get_Coord_y()-self.quaffle.ball.get_Coord_y())**2)<=(self.quaffle.ball.radius)**2:
                                self.quaffle.is_caught_by_hunter(i.player)
                                break
                            else:
                                self.quaffle.ball.none_is_posessing()
            else:
                for i in self._hunters:
                    if ((i.player.get_Coord_x()-self.quaffle.ball.get_Coord_x())**2+(i.player.get_Coord_y()-self.quaffle.ball.get_Coord_y())**2)<=(self.quaffle.ball.radius)**2:
                        self.quaffle.is_caught_by_hunter(i.player)
                        break
                    else:
                        self.quaffle.ball.none_is_posessing()

    def check_snitch(self):
        for i in self._seekers:
            if ((i.player.get_Coord_x()-self.snitch.ball.get_Coord_x())**2+(i.player.get_Coord_y()-self.snitch.ball.get_Coord_y())**2)<=(self.snitch.ball.radius)**2:
                self.snitch.endGame(i.player.type)

    def check_score(self):
        if self.quaffle.ball._possession==None:
            for i in self.rings:
                if i.ring.type!=self.quaffle.ball.quaffle_holder_type:
                    if (i.ring.get_Coord_x()-self.quaffle.ball.get_Coord_x())**2+(i.ring.get_Coord_y()-self.quaffle.ball.get_Coord_y())**2<=(self.quaffle.ball.radius)**2:
                        k=(self.quaffle.ball.quaffle_holder_type)-1
                        self.score[k]+=10

    def check_players(self):
        for i in range(0,len(self._hunters)-1):
            for j in range(i+1,len(self._hunters)):
                if (self._hunters[j].player.get_Coord_x()-self._hunters[i].player.get_Coord_x())**2+(self._hunters[j].player.get_Coord_y()-self._hunters[i].player.get_Coord_y())**2<=(self._hunters[i].player.main_radius)**2:
                    self._hunters[j].player.health-=10
                    self._hunters[j].player.health-=10
                elif (self._hunters[j].player.get_Coord_x()-(self._hunters[i].player.get_Coord_x()+self._hunters[i].player.dx1))**2+(self._hunters[j].player.get_Coord_y()-(self._hunters[i].player.get_Coord_y()+self._hunters[i].player.dy1))**2<=(self._hunters[i].player.head_radius)**2:
                    self._hunters[j].player.health-=10
                    self._hunters[j].player.health-=10
                elif (self._hunters[j].player.get_Coord_x()-(self._hunters[i].player.get_Coord_x()+self._hunters[i].player.dx2))**2+(self._hunters[j].player.get_Coord_y()-(self._hunters[i].player.get_Coord_y()+self._hunters[i].player.dy2))**2<=(self._hunters[i].player.hand_radius)**2:
                    self._hunters[j].player.health-=10
                    self._hunters[j].player.health-=10
            for m in self._seekers:
                if (m.player.get_Coord_x()-self._hunters[i].player.get_Coord_x())**2+(m.player.get_Coord_y()-self._hunters[i].player.get_Coord_y())**2<=(self._hunters[i].player.main_radius)**2:
                    self._hunters[j].player.health-=10
                    self._hunters[j].player.health-=10
                elif (m.player.get_Coord_x()-(self._hunters[i].player.get_Coord_x()+self._hunters[i].player.dx1))**2+(m.player.get_Coord_y()-(self._hunters[i].player.get_Coord_y()+self._hunters[i].player.dy1))**2<=(self._hunters[i].player.head_radius)**2:
                    self._hunters[j].player.health-=10
                    self._hunters[j].player.health-=10
                elif (m.player.get_Coord_x()-(self._hunters[i].player.get_Coord_x()+self._hunters[i].player.dx2))**2+(m.player.get_Coord_y()-(self._hunters[i].player.get_Coord_y()+self._hunters[i].player.dy2))**2<=(self._hunters[i].player.hand_radius)**2:
                    self._hunters[j].player.health-=10
                    self._hunters[j].player.health-=10

    def update(self,ct):
        self.check_if_on_screen()
        self.check_quaffle()
        self.check_snitch()
        self.check_score()
        self.check_players()