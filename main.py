import pygame; 
from settings import Settings;
# import sys; 
from background import Background; 
import game_functions as gf;

pygame.init();
game_settings = Settings(); 
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("Plants V Zombies");
background = Background(game_settings); 


def run_game():
	while 1: 
		gf.check_events(screen, game_settings); 
		screen.fill(game_settings.bg_color); 
		pygame.display.flip(); 


run_game(); 










