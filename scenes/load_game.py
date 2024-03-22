import os
import pygame
from pygame.locals import *
from constants import *
from scripts.button_handler import *
from scripts.frames import *

class LoadGame:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.SysFont(MENU_FONT, MENU_FONT_SIZE // 2)
        self.background = pygame.image.load("assets/background/Scenery_Main_Menu.png").convert()
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))
        
        self.frame_saved_games = pygame.image.load("assets/village/Frame_Background.png").convert_alpha()
        self.frame_saved_games = pygame.transform.scale(self.frame_saved_games, (self.screen.get_width() * 0.4, self.screen.get_height() * 0.8))
        self.frame_saved_games_border = Frames.frame_border(self.frame_saved_games)
        self.saved_games_y = 0
        
        self.frame_small = pygame.image.load("assets/village/Frame_Background.png").convert_alpha()
        self.frame_small = pygame.transform.scale(self.frame_small, (self.screen.get_width() * 0.4, self.screen.get_height() * 0.4))
        self.frame_small_border = Frames.frame_border(self.frame_small)
        
        self.saved_games = self.load_saves()
        self.selected_option = 0 if len(self.saved_games)>0 else -1
        
        self.options_text_list, self.rectangles_list = Frames.in_frame_options(self.saved_games, self.font, self.screen.get_width() * 0.55, self.screen.get_height() * 0.1)
        
    def load_saves(self):
        saved_games_path = r'data/saved_games'
        saved_games = os.listdir(saved_games_path)
        saved_games_paths = [os.path.join(saved_games_path, folder) for folder in saved_games]
        sorted_saved_games_paths = sorted(saved_games_paths, key=lambda x: os.path.getmtime(x), reverse=True)
        sorted_saved_games = [os.path.basename(folder) for folder in sorted_saved_games_paths]
        return sorted_saved_games
    
    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.back_button_rect = ButtonHandler.generate_frame(self.screen, 'Back', self.font, (self.screen.get_width() // 10, self.screen.get_height()  // 10), True)
        self.play_button_rect = ButtonHandler.generate_frame(self.screen, 'Play', pygame.font.SysFont(MENU_FONT, MENU_FONT_SIZE), (self.screen.get_width() * 0.25, self.screen.get_height() * 0.3), True)
        
        # Saved games
        self.screen.blit(self.frame_saved_games, (self.screen.get_width() * 0.55, self.screen.get_height() * 0.1))
        self.screen.blit(self.frame_saved_games_border, (self.screen.get_width() * 0.55 - FRAME_BORDER_THICKNESS, self.screen.get_height() * 0.1 - FRAME_BORDER_THICKNESS))
        
        if len(self.saved_games)>0:
            for index, (option, text_surface) in enumerate(self.options_text_list):
                text_rect = self.rectangles_list[index]
                if index == self.selected_option:
                    self.screen.blit(self.font.render(option, True, MENU_HIGHLIGHT_COLOR), text_rect.topleft)
                else:
                    self.screen.blit(text_surface, text_rect.topleft)
        
        # Options and game info
        self.screen.blit(self.frame_small, (self.screen.get_width() * 0.05, self.screen.get_height() * 0.5))
        self.screen.blit(self.frame_small_border, (self.screen.get_width() * 0.05 - FRAME_BORDER_THICKNESS, self.screen.get_height() * 0.5 - FRAME_BORDER_THICKNESS))
        
    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.go_back()
            elif event.key == pygame.K_UP and len(self.saved_games)>0:
                self.selected_option = (self.selected_option - 1) % len(self.options_text_list)
            elif event.key == pygame.K_DOWN and len(self.saved_games)>0:
                self.selected_option = (self.selected_option + 1) % len(self.options_text_list)

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                
                if self.back_button_rect.collidepoint(mouse_pos):
                    self.go_back()
            
            if len(self.saved_games)>0:
                for index, rect in enumerate(self.rectangles_list):
                    if rect.collidepoint(mouse_pos):
                        self.selected_option = index
                        print(self.selected_option)
        
        self.display()
                    
    def go_back(self):
        self.game.change_scene('MainMenu')