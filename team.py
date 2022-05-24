import pygame 
from player import *

class Team:
    def __init__(self,group):
        #self.type = team_type
        self.player=[]
        self.group=group

    def add_players(self,player):
        self.player.append(player)


    def _findPlayer(self, position): 
        for player in self: 
            if player.type == position:
                return player
        return None

    def get_player(self, position):
        if position in ('hunter', 'seeker'):
            return self._findPlayer(position)

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
    def __init__(self,team:Team):
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
        for player in self.team.group:
            if player!=from_player:
                if (from_player.pos.distance_to(player.pos) < from_player.pos.distance_to(pos)):
                    closest=player
                    pos=player.pos
        print(closest)
        if from_player.quaffle!=None:
            print('***')
            from_player.quaffle.passing(closest)


    def update(self,time):

        if self.team.player[0].activity==1:
            self.active_player=self.team.player[0]

        if self.team.player[1].activity==1:
            self.active_player=self.team.player[1]

        if self.team.player[0].activity==0:
            self.passive_player=self.team.player[0]

        if self.team.player[1].activity==0:
            self.passive_player=self.team.player[1]

        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:

            if self.team.player[0].activity==1 and self.team.player[1].activity==0 :
                self.active_player=self.team.player[1]
                self.passive_player=self.team.player[0]

            if self.team.player[0].activity==0 and self.team.player[1].activity==1 :
                self.active_player=self.team.player[0]
                self.passive_player=self.team.player[1]

        self.active_player.update(time)
        self.passive_player.computer_update(time)

