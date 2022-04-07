import sys
import pygame
import math
import pygame.locals as local
from vector import Vec2d

class Event:
    def eventHandler(game, player):
        keys = pygame.key.get_pressed()

        if keys[local.K_LEFT]:
            player.changeHeading("left")

        if keys[local.K_RIGHT]:
            player.changeHeading("right")

        if keys[local.K_UP]:
            player.changeHeading("up")

        if keys[local.K_DOWN]:
            player.changeHeading("down")

        if keys[local.K_s]:
            player.pass_quaffle()


        for event in pygame.event.get():
            if event.type == local.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == local.KEYDOWN:
                if event.key == local.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def pixel_collide(first, second):
            offset_x = (first.rect.left - second.rect.left)
            offset_y = (first.rect.top - second.rect.top)
            if (second.mask.overlap(first.mask, (offset_x, offset_y)) != None):
                return True
            else:
                return False

    def circle_collide(first, second):
            between = distance(first, second)
            rad1 = (first.rect.width + first.rect.height) / 2
            rad2 = (first.rect.width + first.rect.height) / 2
            if (between <= (rad1 + rad2)):
                return True

    def collide_player(d_from):
            players = []
            for elem in object_list:
                if elem.type == 'player':
                    players.append(elem)
            for player in players:
                if (circle_collide(d_from, player)):
                    return player
            return None

    def truncate(vector, m):
            magnitude = vector.length
            if (magnitude > m):
                vector *= m / magnitude
            return vector
    def distance(from_sprite, to_sprite):
        return (to_sprite.position - from_sprite.position).get_length()



