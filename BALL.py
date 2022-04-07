import pygame
import controller_hunter
from vector import Vec2d
MAP_WIDTH = 10000
MAP_HEIGHT=10000
GRND_BLOCK_H=64
GRAVITY=0.8

class Ball(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.controlling=controller_hunter.Controller_hunter(game, self)
        self.game = game
        self.position = Vec2d(0, 0)
        self.velocity = Vec2d(0, 0)
        self.acceleration = 0

        self.image = None
        self.rect = pygame.Rect(self.position.x,self.position.y, 0, 0)

    def _update(self):
        #self._Borders() 
        local_x = self.position.x - self.game.camera.x
        local_y = self.position.y - self.game.camera.y
        self.rect = pygame.Rect(local_x,local_y,self.image.get_width(),self.image.get_height())


    def draw(self):
            local_x = self.position.x - self.game.camera.x
            local_y = self.position.y - self.game.camera.y
            self.game.screen.blit(self.image, (local_x, local_y))

    def reset(self):
        self.velocity *= -1
        self.acceleration /= 10


class Quaffle(Ball):
    def __init__(self, game):
        Ball.__init__(self, game)
        self.image = pygame.image.load("quaffle.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.held_by = None

    def update(self):
        self._update()
        DAMPING = 0.3
        gravity_vec = Vec2d(0, GRAVITY).normalized()
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


