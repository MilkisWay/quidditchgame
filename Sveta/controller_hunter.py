import pygame
#import controller
import random
#from Unit_2 import Unit 

class Controller_hunter:
    def __init__(self, game, player,angle):
        self.game = game
        self.player=player
        self.isPaused = False
        self.control = [0,0] #управление
        self.angle = 0


    def seek(self, target, slowingRadius=1):
        self.control += self.doSeek(target, slowingRadius)

    def evade(self, target):
        self.control+= self.doEvade(target)
   
    def get_closest(location, group):
        pass
        closest = Unit(game,team type, [100000,1000000],0)
        for player in group:
            if (distance(d_from.position, elem.position) < distance(d_from.position, closest.position)):
                closest = elem
        return closest


    def reset(self):
        self.control = [0,0]

    def doSeek(self, target, slowingRadius=0):
        desired  = target - self.player.position
        distance = desired.get_length()

        if (distance <= slowingRadius):
            pass
            
        else:
           pass
        


    
 

