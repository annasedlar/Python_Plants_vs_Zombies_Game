import sys; 
import pygame; 
from plant import Plant;
from peashooter import Peashooter;
from gatling import Gatling; 
from bullet import Bullet; 


def check_events(screen, game_settings, squares, plants, bullets, icons): 
	# print 'test'
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print event.type
			mouse_x, mouse_y = pygame.mouse.get_pos(); 
			print mouse_x;
			print mouse_y;

			for square in squares: 
				if square.rect.collidepoint(mouse_x, mouse_y):
					print "square: ", square.square_number; 
					plants.add(Peashooter(screen, square));
					if(game_settings.chosen_plant == 1):
						plants.add(Peashooter(screen,square));
					elif(game_settings.chosen_plant == 2):
						plants.add(Gatling(screen,square));

			for icon in icons:
				if icon.rect.collidepoint(mouse_x,mouse_y):
					game_settings.chosen_plant = icon.slot
					print "You clicked: ",icon.image;
					# plants.add(Peashooter(screen,square));

		elif event.type == pygame.KEYDOWN:
			print event.key
			if event.key == pygame.K_SPACE:
				print "pressed space"
				for plant in plants:
					plant.draw_me();
					bullets.add(Bullet(screen, plant));

		elif event.type == pygame.MOUSEMOTION: 
			print event.pos
			for square in squares:
				if square.rect.collidepoint(event.pos):
					# the sprite (square) itself, which is type Group
					game_settings.highlighted_square = square; 
					print game_settings.highlighted_square;

def update_screen(screen, game_settings, background, zombies, squares, plants, bullets, tick, icons):
	# print 'test';
	screen.blit(background.image, background.rect); 

	for icon in icons:
		screen.blit(icon.image, icon.rect);

	if game_settings.highlighted_square != 0:
		# params for draw: 1. WHERE (screen) 2. COLOR (RGB tuple) 3. coordinates (left, top, width, height (tuple)) 4. radius in px
		pygame.draw.rect(screen, (255, 215, 0), (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top, game_settings.squares['square_width'], game_settings.squares['square_height']), 5)
	

	# draw zombies
	for zombie in zombies.sprites():
		if game_settings.game_active == True:
			zombie.update_me();
		zombie.draw_me();
		if zombie.rect.left <= zombie.screen_rect.left:
			game_settings.game_active = False;

	for plant in plants:
		plant.draw_me();
		print plant.yard_row; 
		# every 1 second = 30 frames
		if tick % 10 == 0:
			if game_settings.zombie_in_row[plant.yard_row] > 0: 
				bullets.add(Bullet(screen, plant));
			

	for bullet in bullets.sprites():
		bullet.update_me(); 
		bullet.draw_me(); 


















