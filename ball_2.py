import pygame
from pygame.sprite import Sprite
from random import randint
from unit import Unit

class Ball (Unit):
	def __init__(self,set,screen):
		#self.r=r
		#self.x=xPos 
		#self.y=yPos
		self.x=0
		self.y=0
		self.dx=1
		self.dy=1
		self.image = set.ball_image
		self.rect=self.image.get_rect()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		#self.dx=2
		#self.dy=2
		self.number = set.ball_number
		self.rect_width=self.rect.width
		self.rect_height=self.rect.height
		distant_x = randint(10,50) * self.rect_width
		distant_y = randint(0,10) * self.rect_height
		self.rect.y=0
		self.rect.x=0
		self.score=score
	
	def fall_ball(self, set):
		self.rect.y += set.ball_speed

	def change_ball(self, set):
		distant_x = randint(10,50) * self.rect_width
		distant_y = randint(0,10) * self.rect_height
		self.rect.x = self.screen_rect.centerx + distant_x
		self.rect.y = 0
	
	def update(self):
		self.rect.x+=randint(-100,100)
		self.rect.y+=randint(-100,100)
		if (self.rect.x<=0):
			self.dx*=-1
		if (self.rect.y<=0):
			self.dy*=-1
	

	def draw_ball(self,ball):
		self.screen.blit(self.image,self.rect)
			
	def collideBalls(self,unit):
		for ball in balls:
			if unit_rect.collidepoint(ball.rect.center):
				self_score += ball.score
				ball.kill()


	def update_ball(ball, unit, set):
		if pygame.sprite.collide_rect(ball ,unit): 
			ball.change_ball(set)
			set.catch_number += 1
		if check_ball_border(ball, set): 
			if ball.number > 0:
				ball.number -= 1
				ball.change_ball(set)
			else:
				set.finish = True

	def check_ball_border(ball, set):
		if ball.rect.bottom >= set.bg_height:
			 return True
		else:
			return False


