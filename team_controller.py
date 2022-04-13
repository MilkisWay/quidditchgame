import pygame
import math
import random
import pygame.locals as local

#Зачем он тебе? В PlayState это всё делается!
#Там надо только контроллеры вызвать и всё! Это уже не контроллер, который мы обсуждали! А сама игра!


class Team_controller:
    def __init__(self):
        self.players = pygame.sprite.Group()
        self.teams = []
        self.rings = []
        self.quaffle = None


    def add_team(self, team):
          if team.type not in self.teams:
                self.teams[team.type] = team
                self.all_players.add(team.sprites())

    def update_teams(self,teams):
        for team in teams:
            for player in team:
                player.update() #update unit

    def draw_teams(self):
        for team in self.teams:
            for player in team:
                player.draw()
 

    def draw_rings(self):
        for ring in self.rings:
            for ring in rings:
                ring.draw()






          

  