import pygame; 
from pygame.sprite import Sprite; 
import random;

class Zombie(Sprite): 
	# this is the barebones of a sprite class in python
	def __init__(self, screen, speed, health):
		super(Zombie, self).__init__(); 
		self.speed = speed; 
		self.health = health; 
		self.image = pygame.image.load('./images/Crazyzombie.gif')
		self.image = pygame.transform.scale(self.image, (127, 148));
		self.rect = self.image.get_rect(); 
		self.screen = screen; 
		self.screen_rect = screen.get_rect(); 
		# self.rect.centery = self.screen_rect.centery; 
		self.rect.right = self.screen_rect.right; 

		self.x = float(self.rect.x)

		# find a random row (1-5) 
		randy = random.randint(1,5);
		if randy == 1:
			self.rect.centery = 245
		elif randy == 2:
			self.rect.centery = 350
		elif randy == 3:
			self.rect.centery = 455
		elif randy == 4:
			self.rect.centery = 560
		elif randy == 5:
			self.rect.centery = 665


	def update_me(self):
		self.x -= self.speed * 1; 
		self.rect.x = self.x; 

	def draw_me(self): 
		self.screen.blit(self.image, self.rect);
		
	def hit(self, damage):
		self.health -= damage;











