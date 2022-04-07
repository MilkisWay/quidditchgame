import pygame
import math
import random
import pygame.locals as local
from vector import Vec2d
SCREEN_WIDTH=1600
SCREEN_HEIGHT=900
MAP_WIDTH=5000
CONTROL_USER = 1

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.camera = Camera()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.teams = []
        self.goals = []

        player_controlled=1
        ai_controlled=2 
        management=[]
        management.append(player_controlled)
        management.append(ai_controlled)     
        self.quaffle = None

        #self.player_controlled=1
        #self.ai_controlled=2    

    def add_team(self, team):
        player_controlled=1
        ai_controlled=2
        
        #if (team.type==player_controlled or team.type==ai_controlled):
            #if team.type not in self.teams:
        self.teams.append(team)
       

    def get_team(self, type_or_player):
        if type_or_player in (player_controlled, ai_controlled):
            return self.teams[type_or_player]
        else:
            for team in self.teams.values():
                if type_or_player in team:
                    return team

    def update_teams(self,teams):
        for team in teams:
            for player in team:
                player.update()

    def draw_teams(self):
        for team in self.teams:
            for player in team:
                player.draw()

    def add_goal(self, goal, team):
        if team in self.goals:
            self.goals[team].append(goal)
            

    #def get_goal(self, player, my_or_opp=1):
        #if my_or_opp:
            #return self.goals[player.opposition][int(math.floor(random.random() * 3))]
        #else:
            #return self.goals[player.team][int(math.floor(random.random() * 3))]

    def draw_goals(self):
        for goal in self.goals:
            for goal in goals:
                goal.draw()


class Team(pygame.sprite.Group):
    def __init__(self, team_type):
        super().__init__(self)
        self.type = team_type

    def _findPlayer(self, position):
        for player in self:
            if player.type == position:
                return player
        return None

    def get_player(self, position):
        if position in (keeper, seeker):
            return self._findPlayer(position)
    

    def set_first_control(self):
        temp = self._findPlayer("chaser")
        temp.controller = CONTROL_USER
        return temp

    def get_group(self, group_name):
        theGroup = []
        if group_name in ("chaser", "beater"):
            for player in self:
                if player.type == group_name:
                    theGroup.append(player)
        return theGroup

class Goal(pygame.sprite.Sprite):
    def __init__(self, game, position):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.position = position
        self.image = pygame.image.load("goal.png")
        self.rect = local.Rect(self.position.x,self.position.y,self.image.get_width(), self.image.get_height())

    def draw(self):
        if self.game.camera.onScreen(self):
            local_x = self.position.x - self.game.camera.x
            local_y = self.position.y - self.game.camera.y
            self.game.screen.blit(self.image, (local_x, local_y))

  
class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.track = None

    def onScreen(self, sprite):
        top_left = (sprite.position.x >= self.x and sprite.position.x <= (self.x + SCREEN_WIDTH)) and ((sprite.position.y >= self.y and sprite.position.y <= (self.y + SCREEN_HEIGHT)))
        top_right = (sprite.position.x + sprite.image.get_width() >= self.x and
                  sprite.position.x + sprite.image.get_width() <= (self.x + SCREEN_WIDTH)) and (
                (sprite.position.y >= self.y and
                 sprite.position.y <= (self.y + SCREEN_HEIGHT)))
        return top_left or top_right

    def update(self):
        MAP_HEIGHT=1024
        if self.track:
            self.x = self.track.position.x - SCREEN_WIDTH / 2
            self.y = self.track.position.y - SCREEN_HEIGHT / 2

            if self.x < 0:
                self.x = 0
            elif (self.x + SCREEN_WIDTH) > MAP_WIDTH:
                self.x = MAP_WIDTH - SCREEN_WIDTH
            if self.y < 0:
                self.y = 0
            elif (self.y + SCREEN_HEIGHT) > MAP_HEIGHT:
                self.y = MAP_HEIGHT - SCREEN_HEIGHT
