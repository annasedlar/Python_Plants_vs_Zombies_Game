import pygame; 
from settings import Settings;
# import sys; 
from background import Background; 
import game_functions as gf;
from pygame.sprite import Group, groupcollide; 
from zombie import Zombie;
from square import Square;
from plant_icon import Plant_Icon;
from start_button import Start_Button;

pygame.init();
game_settings = Settings(); 
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("Plants V Zombies");
background = Background(game_settings); 
peashooter_icon = Plant_Icon(game_settings, 'peashooter.png', 1);
gatling_icon = Plant_Icon(game_settings, 'Gatling_Pea_Fixed.png', 2);
icons = [peashooter_icon, gatling_icon];
start_button = Start_Button(screen); 
# our groups
zombies = Group(); 
plants = Group(); 
squares = Group(); 
bullets = Group(); 

# load our squares with our vars
for i in range(0,5):
	for j in range(0,9):
		squares.add(Square(screen, game_settings, i, j));

def run_game():
	tick = 0; 
	while 1: 
		# print game_settings.game_active;
		gf.check_events(screen, game_settings, start_button, squares, plants, bullets, icons); 
		if game_settings.game_active == True:
			# screen.fill(game_settings.bg_color); 
			tick += 1; 
			if tick % 30 == 0:
				zombies.add(Zombie(screen, game_settings));

			plants_died = groupcollide(plants, zombies, True, True);
			zombies_hit = groupcollide(zombies, bullets, False, True);
			# zombies_died = groupcollide(zombies, bullets, True, True);

			for zombie in zombies_hit:
				# print zombie; 
				# print zombies_hit[zombie];
				if zombie.yard_row == zombies_hit[zombie][0].yard_row:
					bullets.remove(zombies_hit[zombie][0]);
					print "same row!"
					# the zombie took 1 unit damage
					zombie.hit(1);
					if zombie.health <= 0:
						zombies.remove(zombie); 
						game_settings.zombie_in_row[zombie.yard_row] -= 1; 
						game_settings.zombies_killed +=1; 

		gf.update_screen(screen, game_settings, start_button, background, zombies, squares, plants, bullets, tick, icons);
		pygame.display.flip();

	if plants_died: 
		print "*************************************"
		print "*************************************"
		print "************YOU LOST!****************"
		print "*************************************"
		print "*************************************"
	if game_settings.game_active == False:
		start_button.draw_button();


run_game(); 










