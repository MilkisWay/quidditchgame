import pygame 

class Team(pygame.sprite.Group):
    def __init__(self,players):
        pygame.sprite.Group.__init__(self)
        #self.type = team_type
        self.all_players = pygame.sprite.Group()
        self.teams=[]
    

    def _findPlayer(self, position): #position: hunter or seeker
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


class Team_controller:
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.teams = []
        self.rings =[]

    def add_team(self, team):
            if team.type not in self.teams:
                self.teams[team.type] = team
                self.all_players.add(team.sprites())


    def get_team(self, player_type):
        if player_type in ('player_controlled', 'computer_controlled'):
            return self.teams[player_type]
        else:
            for team in self.teams:
                if player_type in team:
                    return team

    def update_teams(self):
        for team in self.teams:
            for player in team:
                player._update()

class Team_view:
    def __init__(self,Team_controller):
        self.teams = []

    def draw_teams(self):
        for team in self.team:
            for player in team:
                player._render()

