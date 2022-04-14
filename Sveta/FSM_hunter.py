import pygame
from FSM_base import FSM

class FSM_hunter(FSM):
    def __init__(self, actual):
        FSM_base.__init__(self, actual)
        self.push(self.quaffle_no)


    def quaffle_no(self):

        hunter= self.game.get_team(self.actual).get_group('chaser')
        closest_chaser = groupClosest(my_chasers, self.game.quaffle)
        #self.actual.controller_hunter.collisionAvoidance()

 
        if closest_chaser == self.actual:
            self.pop()
            self.push(self.get_quaffle) # изменяется состояние если поймат шар
            return
       # else:
            #self.pop()
            #self.push(self.get_quaffle)
            #self.push(self.support_attack)
            #return

