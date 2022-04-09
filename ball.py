import pygame
import os
import sys
from pygame.locals import *

class BallModel(object):
    def __init__ (self,pos_x,pos_y,speed):
        self.pos = pygame.math.Vector2(pos_x,pos_y)
        self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
        self.speed = pygame.math.Vector2(speed,speed)
        self.g=9.8

class BallController(object):
    def __init__(self):
        self.balls = []

    def addBall(self,pos,speed):
        self.balls.append(BallModel(pos,speed))

    def fly():
        pass

class BallView(object):
    def __init__(self, ballController, img):
        self.BallController = ballController
        self.image = pygame.image.load(img)
    def render(self, surface):
        for i in self.BallController.balls:
            surface.blit(self.image,self.BallController.balls[i].pos)


class Quaffle(Ball):
    def __init__(self, game):
        Ball.__init__(self, game)
        self.image = pygame.image.load("quaffle.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.held_by = None

    def update(self):
        self._update()
        DAMPING = 0.3
        gravity_vec = Vec2d(0, GRAVITY).normalized()#whaaaaat&&
        self.velocity += gravity_vec * 0.01

        if self.held_by:
            self.position = self.held_by.position.copy()
        else:
            self.position += self.velocity.normalized() * self.acceleration

        if self.acceleration > 1:
            self.acceleration = self.acceleration - DAMPING
        elif self.acceleration < 1:
            self.acceleration = 1

    def draw(self):
        if self.game.camera.onScreen(self):
            local_x = self.position.x - self.game.camera.x
            local_y = self.position.y - self.game.camera.y
            self.game.screen.blit(self.image, (local_x, local_y))

    def setPossession(self, player):
        self.held_by = player

    def getPossession(self):
        return self.held_by

    def throw(self, angle, power):
        self.velocity = angle
        self.acceleration = power
        self.setPossession(None)
    def distance(from_sprite, to_sprite):
        return (to_sprite.position - from_sprite.position).get_length()


