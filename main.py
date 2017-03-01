import pygame; 
from settings import Settings;
# import sys; 
from background import Background; 
import game_functions as gf;
from pygame.sprite import Group, groupcollide; 
from zombie import Zombie;
from square import Square;
# from plant import Plant;

pygame.init();
game_settings = Settings(); 
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("Plants V Zombies");
background = Background(game_settings); 

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
		gf.check_events(screen, game_settings, squares, plants, bullets); 
		gf.update_screen(screen, game_settings, background, zombies, squares, plants, bullets, tick);
		# screen.fill(game_settings.bg_color); 
		tick += 1; 
		if tick % 30 == 0:
			zombies.add(Zombie(screen, game_settings));

		pygame.display.flip();

		plants_died = groupcollide(plants, zombies, True, True);
		zombies_hit = groupcollide(zombies, bullets, False, True);
		# zombies_died = groupcollide(zombies, bullets, True, True);

		for zombie in zombies_hit:
			print zombie; 
			# the zombie took 1 unit damage
			zombie.hit(1);
			if zombie.health <= 0:
				zombies.remove(zombie); 

		pygame.display.flip();

	if plants_died: 
		print "*************************************"
		print "*************************************"
		print "************YOU LOST!****************"
		print "*************************************"
		print "*************************************"



run_game(); 










