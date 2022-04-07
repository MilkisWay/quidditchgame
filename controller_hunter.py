from vector import Vec2d
import controller
import random

class Controller_hunter:
    def __init__(self, game,own):
        self.game = game
        self.own=own
        self.controlling=Vec2d(0,0)

    def seek(self, target, slowingRadius=1):
        self.controlling += self.doSeek(target, slowingRadius)

    def evade(self, target):
        self.controlling += self.doEvade(target)

    def pursuit(self, target):
        self.controlling += self.doPursuit(target)

    def reset(self):
        self.controlling = Vec2d(0, 0)

    def doSeek(self, target, slowingRadius=0):
        desired = target - self.own.position
        distance = desired.get_length()

        if (distance <= slowingRadius):
            desired = desired.normalized() * self.own.max_speed * (distance / slowingRadius)
        else:
            desired = desired.normalized() * self.own.max_speed

        force = desired - self.own.velocity
        return force

    def doPursuit(self, target):
        distance = target - self.own.position
        updatesNeeded = distance.get_length() / self.own.max_velocity
        targetFuturePosition = target + (Vec2d(0, 0) * updatesNeeded)
        return self.doSeek(targetFuturePosition)


    
 

