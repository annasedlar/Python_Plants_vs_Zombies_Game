import pygame.font


class Start_Button():
	def __init__(self,screen):
		# get the screen and save it to this location
		self.screen = screen;
		# get screen size and location
		self.screen_rect = screen.get_rect();

		self.width = 250; 
		self.height = 100; 

		self.button_color = 0, 200, 150; 
		self.text_color = 255, 255, 255; 
		self.font = pygame.font.Font(None,52);

		# set the rect of the button (rect is the substance of the button)
		self.rect = pygame.Rect(0, 0, self.width, self.height); 
		# set loc of button (center of screen)
		self.rect.center = self.screen_rect.center; 
		self.setup_message(); 

	def setup_message(self): 
		# turn text into an image
		self.image_message = self.font.render("Play", True, self.text_color);
		self.image_message_rect = self.image_message.get_rect();
		self.image_message_rect.center = self.rect.center; 

	def draw_button(self): 
		self.screen.fill(self.button_color, self.rect);
		# the WHAT and the WHERE
		self.screen.blit(self.image_message,self.image_message_rect)