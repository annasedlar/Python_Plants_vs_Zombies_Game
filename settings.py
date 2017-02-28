import pygame; 

class Settings(): 
	def __init__(self):
		# set the screen size dynamically - automatically the size of our screen 
		display_info = pygame.display.Info(); 
		self.screen_size = (display_info.current_w, display_info.current_h);
		self.bg_color = (82,111,53); 
		self.zombie_speed = 5; 
		self.zombie_health = 5; 