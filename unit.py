import sys
import pygame

class Unit (pygame.sprite.Sprite):
	#pos_x and pos_y - public 
	def _init_(self,width,height,pos_x,pos_y,color):
		super().__init__()
		#speed as constant in non-playable objects
		self.image =pygame.Surface([width,height])
		#self.image.fill(color)
		self.rect=self.image.get_rect()
		self.score=0
#functions
def move():
	pass
def update(self):
		self.gravitation()
def render():
	pass

		
class Player (Unit):

	def __init__(self,width,height,moving,catching,radious,falling):
		super().__init__()
#functions
def move():
	pass
def update(self):
		self.gravitation()
def render():
	pass
