import pygame
import os
import sys
from pygame.locals import *
from interstitial import *

class CollisionController(object):
    def __init__(self):
        self.hunters=[]
        self.quaffle=None
        self.score=None
        self.basic=None
        self._seekers=[]
        self.snitch=None
        self.rings=[]
        self.closest_hunter_to_quffle=None
        self.min_distance_to_quaffle=10000000000000
        self.scores=[0,0]

    def add_basic_setup(self,object1):
        self.basic=object1

    def add_hunter(self,object1):
        self.hunters.append(object1)

    def add_seeker(self,object1):
        self._seekers.append(object1)

    def add_score_for_team(self,object1):
        self.score=object1

    def add_quaffle(self,object1):
        self.quaffle=object1

    def add_ring(self,object1):
        self.rings.append(object1)

    def add_snitch(self,object1):
        self.snitch=object1

    def check(self,object1):

        if object1.get_Coord_x()>=self.basic.screen_width:
            object1.set_Coord_x(object1.get_Coord_x()-10)
        elif object1.get_Coord_x()<=10:
            object1.set_Coord_x(object1.get_Coord_x()+10)
        if object1.get_Coord_y()>=self.basic.screen_height:
              object1.set_Coord_y(object1.get_Coord_y()-10)
        elif object1.get_Coord_y()<=10:
                object1.set_Coord_y(object1.get_Coord_y()+10)


    def check_for_players(self,object1):

        if object1.pos.x>=self.basic.screen_width:
            object1.pos.x=object1.pos.x-10
        elif object1.pos.x<=10:
            object1.pos.x=object1.pos.x+10
        if object1.pos.y>=self.basic.screen_height:
              object1.pos.y=object1.pos.y-10
        elif object1.pos.y<=10:
                object1.pos.y=object1.pos.y+10

    def check_if_on_screen(self):
        for i in self.hunters:
            self.check_for_players(i.player)
        for i in self._seekers:
            self.check_for_players(i.player)
        self.check(self.quaffle.ball)
        self.check(self.snitch.ball)

    def check_quaffle(self):

        if self.quaffle.ball.possession==True:
            if self.quaffle.ball.quaffle_holder_type == 1:
                mousestate=pygame.mouse.get_pressed()
                if mousestate[0]:
                    if self.distance_to_ring(1)==True:
                        self.quaffle.ball.set_pos(self.rings[1].ring.pos)
                        self.scores[0]+=10
                        self.quaffle.ball.none_is_possessing()
                        self.quaffle.ball.pos.x=500
                        self.quaffle.ball.pos.y=500
                        self.quaffle.update2()

                    else:
                        for i in self.hunters:
                            if i.player.type == 1:
                                if i.player!=self.quaffle.hunter:
                                    if self.distance_to_object(i) < self.min_distance_to_quaffle:
                                        self.min_distance_to_quaffle = self.distance_to_object(i)
                                        self.closest_hunter_to_quaffle=i.player

                        if self.closest_hunter_to_quaffle!=None:
                            self.quaffle.is_caught_by_hunter(self.closest_hunter_to_quaffle)
                            self.min_distance_to_quaffle=100000000
                            self.closest_hunter_to_quaffle=None
                            self.quaffle.ball.update()

                        elif self.closest_hunter_to_quaffle==None:
                            self.quaffle.ball.none_is_possessing()
                            self.quaffle.update2()
                else:
                    for i in self.hunters:
                        if i.player.type == 1:
                            if i.player!=self.quaffle.hunter:
                                if self.distance_to_object(i) < self.min_distance_to_quaffle:
                                    self.min_distance_to_quaffle = self.distance_to_object(i)
                                    self.closest_hunter_to_quaffle=i.player

                    if self.closest_hunter_to_quaffle!=None:
                        self.quaffle.radius_of_hunters(self.closest_hunter_to_quaffle)
                        self.min_distance_to_quaffle=100000000
                        self.closest_hunter_to_quaffle=None
                        self.quaffle,ball.update()
                    else:
                        self.quaffle.ball.none_is_possessing()
                        self.quaffle.update2()

            if self.quaffle.ball.quaffle_holder_type == 2:
                if self.distance_to_ring(0)==True:
                        self.quaffle.ball.set_pos(self.rings[0].ring.pos)
                        self.scores[1]+=10
                        self.quaffle.ball.none_is_posessing()
                        self.quaffle.ball.pos.x=500
                        self.quaffle.ball.pos.y=500
                        self.quaffle.update2()
                else:
                    if self.quaffle.hunter.count%10==0:
                        for i in self.hunters:
                            if i.player.type == 2:
                                if i.player!=self.quaffle.hunter:
                                    if self.distance_to_object(i) < self.min_distance_to_quaffle:
                                        self.min_distance_to_quaffle = self.distance_to_object(i)
                                        self.closest_hunter_to_quaffle=i.player

                        if self.closest_hunter_to_quaffle!=None:
                            self.quaffle.is_caught_by_hunter(self.closest_hunter_to_quaffle)
                            self.min_distance_to_quaffle=100000000
                            self.closest_hunter_to_quaffle=None
                            self.quaffle.update()
                        else:
                            self.quaffle.ball.none_is_possessing()
                            self.quaffle.update2()
                    else:
                        for i in self.hunters:
                            if i.player.type == 2:
                                if i.player!=self.quaffle.hunter:
                                    if self.distance_to_object(i) < self.min_distance_to_quaffle:
                                        self.min_distance_to_quaffle = self.distance_to_object(i)
                                        self.closest_hunter_to_quaffle=i.player
                        self.quaffle.radius_of_hunters(self.closest_hunter_to_quaffle)
                        self.min_distance_to_quaffle=100000000
                        self.closest_hunter_to_quaffle=None
        
        if self.quaffle.ball.possession==False:
            for i in self.hunters:
                self.compare_with_object(i)
            if self.closest_hunter_to_quaffle!=None:
                self.quaffle.is_caught_by_hunter(self.closest_hunter_to_quaffle)
                self.min_distance_to_quaffle=100000000
                self.closest_hunter_to_quaffle=None
                self.quaffle.update()
            elif self.closest_hunter_to_quaffle==None:
                self.quaffle.update2()

    def compare_with_object(self,i):
        if  self.distance_to_object(i)<=(self.quaffle.ball.radius):
            if self.distance_to_object(i) < self.min_distance_to_quaffle:
                self.min_distance_to_quaffle = self.distance_to_object(i)
                self.closest_hunter_to_quaffle=i.player


    def distance_to_object(self,i):
        return (((self.quaffle.ball.pos.x - i.player.pos.x) ** 2) + ((self.quaffle.ball.pos.y- i.player.pos.y) ** 2)) ** (0.5)
                               
    def check_snitch(self):
        for i in self._seekers:
            if ((self.snitch.ball.pos.x-i.player.pos.x)**2+(self.snitch.ball.pos.y-i.player.pos.y)**2)**(0.5)<=self.snitch.ball.radius:
                k=(i.player.type)-1
                if self.snitch.ball.count==0:
                    self.scores[k]+=150
                    self.snitch.ball.possession=True
                    self.snitch.ball.gameStop=True
                    self.who_possess = i.player.type
                    self.snitch.ball,count=1
    #def check_score(self):
        #if self.quaffle.ball.possession==False:
            #for i in self.rings:
                #if i.ring.type!=self.quaffle.ball.quaffle_holder_type:
                    #if (i.ring.get_Coord_x()-self.quaffle.ball.get_Coord_x())**2+(i.ring.get_Coord_y()-self.quaffle.ball.get_Coord_y())**2<=(self.quaffle.ball.radius)**2:
                        #k=(self.quaffle.ball.quaffle_holder_type)-1
                        #self.score[k].change_score(10)

    #def check_players(self):
       # for i in range(0,len(self.hunters)-1):
            #for j in range(i+1,len(self._hunters)):
               # if ((self._hunters[i].player.pos.x-self._hunters[j].player.pos.x)**2+(self._hunters[i].player.pos.y-self._hunters[j].player.pos.y)**2)**(0.5)<=(self._hunters[i].player.main_radius):
                   # self._hunters[i].player.health-=1
                   # self._hunters[j].player.health-=1
                #elif ((self._hunters[i].player.pos.x-(self._hunters[j].player.pos.x+self._hunters[j].player.dx1))**2+(self._hunters[i].player.pos.y-(self._hunters[j].player.pos.y+self._hunters[j].player.dy1))**2)**(0.5)<=(self._hunters[i].player.head_radius):
                  #  self._hunters[i].player.health-=1
                   # self._hunters[j].player.health-=1
                #elif (self._hunters[j].player.get_Coord_x()-(self._hunters[i].player.get_Coord_x()+self._hunters[i].player.dx2))**2+(self._hunters[j].player.get_Coord_y()-(self._hunters[i].player.get_Coord_y()+self._hunters[i].player.dy2))**2<=(self._hunters[i].player.hand_radius)**2:
                   # self._hunters[i].player.health-=1
                   # self._hunters[j].player.health-=1
           # for m in self._seekers:
               # if (m.player.get_Coord_x()-self._hunters[i].player.get_Coord_x())**2+(m.player.get_Coord_y()-self._hunters[i].player.get_Coord_y())**2<=(self._hunters[i].player.main_radius)**2:
                   # self._hunters[i].player.health-=1
                   # self._hunters[j].player.health-=1
               # elif (m.player.get_Coord_x()-(self._hunters[i].player.get_Coord_x()+self._hunters[i].player.dx1))**2+(m.player.get_Coord_y()-(self._hunters[i].player.get_Coord_y()+self._hunters[i].player.dy1))**2<=(self._hunters[i].player.head_radius)**2:
                  #  self._hunters[i].player.health-=1
                   # self._hunters[j].player.health-=1
               # elif (m.player.get_Coord_x()-(self._hunters[i].player.get_Coord_x()+self._hunters[i].player.dx2))**2+(m.player.get_Coord_y()-(self._hunters[i].player.get_Coord_y()+self._hunters[i].player.dy2))**2<=(self._hunters[i].player.hand_radius)**2:
                   # self._hunters[i].player.health-=1
                   # self._hunters[j].player.health-=1

    def update(self,ct):
        self.check_if_on_screen()
        self.check_quaffle()
        self.check_snitch()
        #self.check_score()
        #self.check_players()

    def distance_to_ring(self,i):
        if (((self.quaffle.ball.pos.x - self.rings[i].ring.pos.x) ** 2) + ((self.quaffle.ball.pos.y - self.rings[i].ring.pos.y) ** 2)) ** (0.5) <= 500:
            return True

    def render(self,surface):
        f1=pygame.font.Font(None,72)
        surface.blit(f1.render(str(self.scores[0]),True,(255, 223, 100)),(1800,50))
        surface.blit(f1.render(":",True,(255, 223, 79)),(1750,50))
        surface.blit(f1.render(str(self.scores[1]),True,(255, 223, 100)),(1650,50))