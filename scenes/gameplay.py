import pygame
from pygame.locals import *
from constants import *
from scripts.button_handler import *
from scripts.image_handler import *

from scenes.village import Village
from scenes.map import Map

class Gameplay:
    def __init__(self, screen, game):
        self.screen = screen
        self.font = pygame.font.SysFont(MENU_FONT, BAR_FONT_SIZE) 
        self.game = game
        
        self.bar_options = ['Village', 'Review', 'Map', 'Reports', 'Ranking', 'speed_game', 'Tribe', 'Statistics', 'Options', 'Exit']
        self.bar_options_rect = [] # fill this in code later
        self.bar = self.create_bar()
        
    def create_bar(self):
        WIDTH = self.screen.get_width()
        HEIGHT = self.screen.get_height()
        background = pygame.image.load(r'assets\background\Background3.png').convert()
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        background.blit(background, (0, 0)) # WIDTH, bar.get_height()
        
        bar = pygame.image.load("assets/village/Bar.png").convert()
        bar = pygame.transform.scale(bar, (WIDTH, HEIGHT * 0.08))
        background.blit(bar, (0, 0))
        
        option_width = WIDTH // len(self.bar_options)
        current_width = option_width // 2
        
        for option in self.bar_options:
            pos = (current_width, bar.get_height()//2)
            button_rect = ButtonHandler.bar_button(background, option, pos)
            self.bar_options_rect.append((option, button_rect))
            current_width += option_width 
        
        return background
        
        
    def display(self):
        self.screen.blit(self.bar, (0,0))
        try:
            self.current_subscene.display()
        except:
            pass
        
    def handle_event(self, event):
        try:
            self.current_subscene.handle_event(event)
        except:
            pass
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for option, rect in self.bar_options_rect:
                if rect.collidepoint(mouse_pos):
                    if option == 'Exit':
                        self.game.change_scene("MainMenu")
                    else:
                        self.change_scene(option)
                    print(option)  # Wypisz nazwę opcji po kliknięciu

    def change_scene(self, scene_name):
        scene_class = globals().get(scene_name)
        if scene_class:
            print(scene_class)
            self.current_subscene = scene_class(self.screen, self)
        else:
            print(f"Error: Scene '{scene_name}' not found.")
