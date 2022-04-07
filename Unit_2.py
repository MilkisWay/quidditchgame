import pygame
import pygame.locals as local
from controller_hunter import Controller_hunter
from Event import Event
import math
import Game_2
import random
from vector import Vec2d

MAP_HEIGHT=1000
MAP_WIDTH= 100
GRND_BLOCK_H=64

player_controlled=1
ai_controlled=2

class Unit(pygame.sprite.Sprite):
    def __init__(self, game, team):
        pygame.sprite.Sprite.__init__(self)
        self.controllers = Controller_hunter(game, self)

        self.game = game
        self.team = team
        self.type = None
       

        if (team == ai_controlled): 
            self.opposition = player_controlled
        else:
            self.opposition =ai_controlled
        self.opposition = player_controlled
        self.position = Vec2d(10,10)
        self.velocity = Vec2d(0, 0)
        self.new_velocity = Vec2d(0, 0)
        self.acceleration = 0
        self.ai_acceleration = 2

        self.controller = 2

        if self.team == player_controlled:
            self.start_image = pygame.image.load("player.jpg").convert_alpha()
        else:
            self.start_image = pygame.image.load("opposition.png").convert_alpha()
        self.image = self.start_image
        self.rect = local.Rect(self.position.x, self.position.y,self.image.get_width(),self.image.get_height())
        self.mask = pygame.mask.from_surface(self.image)

        self.pointing = -1

        self.max_see_ahead = 50
        self.max_avoid_force = 5
        self.max_force = 5
        self.max_velocity = 10
        self.mass = 5
        self.speed = 0

        self.drawBounds = False

    def changeHeading(self, direction):
        if self.controller == 2:
            return

        if direction == "left":
            vec = Vec2d(-1, 0)
        elif direction == "right":
            vec = Vec2d(1, 0)
        elif direction == "up":
            vec = Vec2d(0, -1)
        elif direction == "down":
            vec = Vec2d(0, 0.1)
        self.acceleration += 0.4

        if self.acceleration > self.max_speed:
            self.acceleration = self.max_speed
        elif self.acceleration < 0:
            self.acceleration = 0

        if (vec.x < 0 and self.pointing == 1):
            self.acceleration -= 0.2
            if self.acceleration <= 0:
                self.velocity.x *= -1
        elif (vec.x > 0 and self.pointing == -1):
            self.acceleration -= 0.2
            if self.acceleration <= 0:
                self.velocity.x *= -1

        self.velocity += vec
        self.velocity = self.velocity.normalized()

 
    def _update(self):
        DAMPING = 0.3
        self.checkCollisions()
        if self.controller == 2:
            #self.controllers.update()
            if self.acceleration > 0:
                self.acceleration = self.acceleration - DAMPING
            elif self.acceleration < 0:
                self.acceleration = 0

        if self.controller == 1:
            self.position += Event.truncate((self.velocity.normalized() *self.acceleration),self.max_speed)

        local_x = self.position.x - self.game.camera.x
        local_y = self.position.y - self.game.camera.y
        self.rect = local.Rect(local_x, local_y,self.image.get_width(),self.image.get_height())
        self.drawBounds = False

    def _inBounds(self):
        if (self.position.x <= 0):
            self.position.x = 3
            self.reset()
        if (self.position.x + self.start_image.get_width() > (MAP_WIDTH)):
            self.position.x = MAP_WIDTH - self.start_image.get_width() - 3
            self.reset()
        if (self.position.y <= 0):
            self.position.y = 3
            self.reset()
        if (self.position.y + self.start_image.get_height() >= (MAP_HEIGHT - GRND_BLOCK_H)):
            self.position.y = MAP_HEIGHT - GRND_BLOCK_H - self.start_image.get_height() - 3
            self.reset()

    def _playerCollisions(self):
        temp_group = self.game.all_players.copy()
        temp_group.remove(self)
        collided_with = pygame.sprite.spritecollideany(self, temp_group)
        temp_group.empty()
        temp_group = None
        if collided_with:
            if Event.pixel_collide(collided_with, self):
                return collided_with

    def checkCollisions(self):
        self._inBounds()
        player_collided = self._playerCollisions()
        if player_collided:
            self.acceleration = 2

    def reset(self):
        self.velocity *= -1
        self.acceleration = 0

    def draw(self):
        if self.game.camera.onScreen(self):
            local_x = self.position.x - self.game.camera.x
            local_y = self.position.y - self.game.camera.y
            self.game.screen.blit(self.image,
                                  (local_x, local_y))
            if self.drawBounds:
                pygame.draw.rect(self.game.screen, (255, 0, 0), self.rect, 1)


class Chaser(Unit):
    def __init__(self, game, team):
        Unit.__init__(self, game, team)
        self.type = "chaser"
        self.acceleration = 0.01

        self.shoot_distance = 500
        self.shoot_power = 30

        self.skill_attack = 5
        self.skill_defend = 8

        self.max_speed = self.max_velocity + math.floor(random.random() * 5)

    def getShootDist(self):
        return self.shoot_distance

    def update(self):
        self._update()

        if self.controller == 2:
            if self.speed < self.max_speed:
                self.speed += self.acceleration
            else:
                self.speed = self.max_speed
       

        if self.controller == 1:
            self.checkQuaffle()

    def checkQuaffle(self):
        if self.game.quaffle.getPossession() is None:
            if Event.pixel_collide(self.game.quaffle, self):
                self.game.quaffle.setPossession(self)

    def shoot(self):
        oppGoal = self.game.get_goal(self)
        vec_between = (oppGoal.position - self.position).normalized()
        self.game.quaffle.throw(vec_between, self.shoot_power)

    def pass_to(self, other):
        vec_between = (other.position - self.position).normalized()
        self.game.quaffle.throw(vec_between, self.shoot_power)

    def pass_quaffle(self):
        if self.pointing == 1:
            self.game.quaffle.position.x = self.position.x + self.start_image.get_width()
        self.game.quaffle.throw(self.velocity, self.shoot_power)

    def tackle(self, oppChaser):
        tackle_chance = math.floor((self.skill_attack + random.random() * 4))
        if tackle_chance > oppChaser.skill_defend:
            return True
        else:
            return False



