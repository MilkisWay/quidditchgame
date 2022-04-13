import pygame
from Unit_2 import Unit
from object import Object

class Seeker(Object):
     def __init__(self, x,y,seg_radius):
        Object.__init__(self, x,y)
        self.seg_radius=1
        self.type = 'seeker'
        self.acceleration = 1
        self.quaffle = None

     def seek(self, target,seg_radius):
        t=target.get_distance()- Seeker.get_distance()

        if (t <= seg_radius):
            t=self.speed * (distance / seg_radius)
        else:
            t=self.speed

        force=t-self.speed
        return force

     def get_quaffle(self):
        self.seek(self.quaffle.position,seg_radius)

        if (Seeker.get_distance(self.get_Coord,self.quaffle.get_Coord) <= self.seg_radius):
                if self.guaffle is None:
                    self.guaffle=1

