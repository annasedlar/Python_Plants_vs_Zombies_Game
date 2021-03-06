import pygame; 

class Settings(): 
	def __init__(self):
		# set the screen size dynamically - automatically the size of our screen 
		display_info = pygame.display.Info(); 
		self.screen_size = (display_info.current_w, display_info.current_h);
		self.bg_color = (82,111,53); 
		self.zombie_speed = 5; 
		self.zombie_health = 50; 
		self.game_active = False; 
		self.chosen_plant = 1; 
		self.zombies_killed = 0; 
		self.game_active = False; 
		self.total_sun = 0;

		# square stuff
		self.squares = {
			"start_left": 367,
			"start_top": 245,
			"square_width": 115,
			"square_height": 105,
			"rows": [
				245,
				350, 
				455,
				560,
				665
			]
		}
		self.highlighted_square = 0;
		self.zombie_in_row = [
			0,
			0,
			0,
			0,
			0
		]
		self.plant_list = [
			'Peashooter',
			'Gatling',
			'Sunflower'
		]