import pygame 
from player import Player
from player import Player_controller

class Team(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        #self.type = team_type
        self.player=[]

    def add_players(self,player):
        self.player.append(player)
        print('team  add players')

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

    def add_controller(self,controller):
        self.players_controller.append(controller)

    def update(self,time):

        if self.team.player[0].activity==1:
            self.active_player=self.team.player[0]
            self.passive_player=self.team.player[1]
        else:
            self.active_player=self.team.player[1]
            self.passive_player=self.team.player[0]

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
             
             if self.active_player ==self.team.player[0]:
                self.active_player = self.team.player[1]
             else:
                self.active_player = self.team.player[0]

        self.active_player.update(time)
        self.passive_player.computer_update(time)

        print(self.team.player[0].activity, self.team.player[1].activity)




            #if self.team.player[0].activity==1 and self.team.player[1].activity==0:
                    #self.team.player[0].activity=0
                    #self.team.player[1].activity=1

                    #self.players_controller[0].computer_update(time)
                    #self.players_controller[1].update(time)

            #if self.team.player[0].activity==0 and self.team.player[1].activity==1:
                    #self.team.player[0].activity=1
                    #self.team.player[1].activity=0
                    
             

                    #self.players_controller[0].update(time)
                    #self.players_controller[1].computer_update(time)

        
        