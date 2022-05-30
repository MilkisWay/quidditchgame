import pygame 
from player import Player
from player import Player_controller
import random

class Team:
    def __init__(self,group):
        #self.type = team_type
        self.player=[]
        self.group=group
        self.group_passive=[]

    def add_players(self,player):
        self.player.append(player)

    def add_activity(self,player):
        self.activity_player=player

    def add_passivity_player(self, player):
        self.passiv_player=player

    def findPlayer(self, position): 
        for player in self: 
            if player.type == position:
                return player
        return None

    def get_player(self, position):
        if position in ('hunter', 'seeker'):
            return self.findPlayer(position)

    def get_group(self, group_name,player):
        Group = []
        if group_name in ('hunter', 'seeker'):
            for player in self:
                if player.type == group_name:
                    Group.append(player)
        return Group

    def get_team(self, player_type):
        if player_type in ('player_controlled', 'computer_controlled'):
            return self.teams[player_type]
        else:
            for team in self.teams:
                if player_type in team:
                    return team

class Team_controller:
    def __init__(self,team:Team,players_controller):
        self.team=team 
        self.players_controller=[]
        self.active_player=None
        self.passive_player=None


    def add_controller(self,controller):
        self.players_controller.append(controller)

    def get_closest(self, from_player):
        pos=pygame.math.Vector2(10000,10000)
        for player in self.team.group:
            if player!=from_player:
                if (from_player.pos.distance_to(player.pos) < from_player.pos.distance_to(pos)):
                    closest=player
                    pos=player.pos

    def throw_closest(self,from_player): #from_player - игрок, у которого сейчас во владении quaffle
        pos=pygame.math.Vector2(10000,10000)
        self.get_closest(from_player)
        if from_player.quaffle!=None:
            from_player.quaffle.passing(closest)

    def update(self,time): #change_activity_player
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_q]:
            if self.team.activity_player.type_name=='hunter':     
                self.team.activity_player=self.team.group[1]
            elif self.team.activity_player.type_name=='seeker':
                self.team.activity_player=self.team.group[0]
        if self.team.activity_player.type_name=='hunter':
                self.team.passiv_player=self.team.group[1]  
        elif self.team.activity_player.type_name=='seeker' :
                self.team.passiv_player=self.team.group[0]
        if self.team.activity_player.type_name=='hunter':
            self.team.activity_player.update(time)
        else:
            self.team.activity_player.update(time)
        if self.team.passiv_player.type_name=='hunter':
            self.team.passiv_player.computer_update_5(time)
        else:
            self.team.passiv_player.computer_update_3(time)
        

