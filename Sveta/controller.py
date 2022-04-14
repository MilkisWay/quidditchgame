import pygame
import controller


class Controller: #Зпчем это отдельно в контроллере? Это должно быть в игроке, раз работаем с ним?
    def __init__(self,player):
        self.player=player
        self.controlling=[]
        #self.fsm
    if self.controlling=='computer_control':
        changeHeading(direction)

    def move(self, direction):
        if direction == "left":
            player.position = [-1, 0]
        elif direction == "right":
             player.position= [1, 0]
        elif player.position == "up":
            player.position= [0, -1]
        elif direction == "down":
            player.position = [0, 0.9]
        self.acceleration += 1

        if self.acceleration < 0:
            self.acceleration = 0


