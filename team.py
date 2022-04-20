import pygame 
from player import Player_controller

class Team(pygame.sprite.Group):
    def __init__(self,players):
        pygame.sprite.Group.__init__(self)
        #self.type = team_type

    def _findPlayer(self, position): #position: hunter or seeker
        for player in self: #Какой игрок в селф? Что просто селф?
            #пробегаем игроками по нашей self команде, если есть игрок на заданной позиции, то возвращаем его
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
    def __init__(self,players_controller):
        self.players_controller = players_controller
        self.players= self.players_controller.players
    
    def add_player_team(self,players):
        team=[]
        team.append(players)
        return team

    def update_teams(self):
        for team in self.teams:
            for player in team:
                player_controller.update()

class Team_view:
    def __init__(self,team_controller):
        self.team_controller = team_controller

    def render(self, surface):
        for i in self.team_controller.players:
            surface.blit(self.team_controller.players.image,(i.get_Coord.x(),i.get_Coord.y()))

