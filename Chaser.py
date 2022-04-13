from Unit_2 import Unit
from Game_2 import Game
from Event import Event 
from BALL import Quaffle

class Chaser(Unit):
    def __init__(self, game, team):
        Unit.__init__(self, game, team)
        self.type = 'chaser'
        self.acceleration = 1
        self.power = 10
        self.quaffle = []

    def add_quaffle(self):
        self.quaffle.append(Quaffle(game))
    
    def check_quaffle(self):
        if self.quaffle.getPossession(self) is None:
                self.quaffle.setPossession(self,player)

    
    def pass_to(self, player):
        dist_between = (player.position - self.position)
        self.quaffle.throw(dist_between, self.power)






