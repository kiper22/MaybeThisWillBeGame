import pygame
from pygame.locals import *
from constants import *
from scripts.button_handler import *
from scripts.image_handler import *
from scripts.frames import *

class Village:
    def __init__(self, screen, gameplay):
        self.screen = screen
        self.font = pygame.font.SysFont(MENU_FONT, MENU_FONT_SIZE) 
        self.gameplay = gameplay
        
        self.village_to_display()

    def village_to_display(self):
        self.village_width_center = self.screen.get_width() * VILLAGE_WIDTH_CENTER
        self.village_image = pygame.image.load("assets/village/Village.png").convert_alpha()
        self.village_image = pygame.transform.scale(self.village_image, (int(self.village_image.get_width() * 0.7), int(self.village_image.get_height() * 0.7)))
    
    def village_info_to_display(self):
        # Village name+points, production, bonusses, troops
        pass
    
    def display(self):
        Frames.big_frame(self.screen, self.village_image, self.village_width_center - self.village_image.get_width() // 2, HEIGHT * 0.1)
        self.screen.blit(self.village_image, (self.village_width_center - self.village_image.get_width() // 2, HEIGHT * 0.1))
        
    def handle_event(self, event):
        pass