import pygame

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
        if position in (...):
            return self._findPlayer(position)
    

    def set_control(self):
        control= self._findPlayer('chaser')
        control.controller = CONTROL_USER
        return control

    def set_group(self, group_name):
        theGroup = []
        if group_name in ('chaser', ... ):
            for player in self:
                if player.type == group_name:
                    theGroup.append(player)
        return theGroup



