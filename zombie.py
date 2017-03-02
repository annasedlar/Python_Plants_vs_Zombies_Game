import pygame; 
from pygame.sprite import Sprite; 
from random import randint;


class Zombie(Sprite): 
	# this is the barebones of a sprite class in python
	def __init__(self, screen, game_settings):
		super(Zombie, self).__init__(); 
		self.speed = game_settings.zombie_speed; 
		self.health = game_settings.zombie_health; 
		self.image = pygame.image.load('./images/Crazyzombie.gif')
		self.image = pygame.transform.scale(self.image, (127, 148));
		self.rect = self.image.get_rect(); 
		self.screen = screen; 
		self.screen_rect = screen.get_rect(); 
		# self.rect.centery = self.screen_rect.centery; 
		self.rect.right = self.screen_rect.right; 
		self.yard_row = randint(0,4);
		self.rect.centery = game_settings.squares['rows'][self.yard_row];
		game_settings.zombie_in_row[self.yard_row] += 1; 

		self.x = float(self.rect.x)
		self.moving = True; 
		self.started_eating = 0; 
		# zombie will take a bite every 2 seconds
		self.damage_time = 2;

		# THREE WAYS TO RANDOMIZE ZOMBIE ROW
		# if you do it this way, must pass squares as a zombie param (and speed/health instead of gamesettings)
		# rand_int = randint(0,45); 
		# i = 0; 
		# print rand_int;
		# for square in squares:
		# 	if i == rand_int:
		# 		bot_coords = square.rect.bottom; 
		# 		self.yard_row = square.row_number; 
		# 		break;
		# 	i += 1; 

		# self.rect.bottom = bot_coords; 
		# self.rect.right = self.screen_rect.right;

		# find a random row (1-5) 
		# randy = randint(1,5);
		# if randy == 1:
		# 	self.rect.centery = 245
		# elif randy == 2:
		# 	self.rect.centery = 350
		# elif randy == 3:
		# 	self.rect.centery = 455
		# elif randy == 4:
		# 	self.rect.centery = 560
		# elif randy == 5:
		# 	self.rect.centery = 665


	def update_me(self):
		if self.moving:
			self.x -= self.speed * 1; 
			self.rect.x = self.x; 

	def draw_me(self): 
		self.screen.blit(self.image, self.rect);

	def hit(self, damage):
		self.health -= damage;

	def zombie_chomp(self, plant):
		plant.health -=1








