import pygame
from pygame.locals import *
from constants import *
from scripts.button_handler import *
from scripts.frames import *

class WorldCreator:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.SysFont(MENU_FONT, MENU_FONT_SIZE // 2)
        self.options = {
            'Map Size': ['Small', 'Medium', 'Large'],
            'Church': ['Yes', 'No'],
            'Watchtower': ['Yes', 'No'],
            'Settlers' : ['Yes', 'No'],
            'Night Mode' : ['Yes', 'No'],
            'Tribes' : ['Yes', 'No'],
            'Map Bonuses' : ['Yes', 'No'],
            'Units Speed' : ['1', '1.2', '1.5', '2'],
            'Production Speed' : ['1', '1.5', '2', '3'],
            'Start Bonus' : ['Yes', 'No'], # 2h o double building speed and production
            'Difficulty': ['Easy', 'Medium', 'Hard'],
            'Winning Conditions' : ['Conquer 80%']
        }
        self.selected_options = {key: value[0] for key, value in self.options.items()}
        self.highlight_states = {option: False for option in self.options}
        self.scroll_y = 0
        self.options_frame = (self.screen.get_height() * 0.2, self.screen.get_height() * 0.8)
        self.background = pygame.image.load('assets/background/Background3.png').convert()
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))

    def display(self):
        self.screen.blit(self.background, (0, 0))
        
        ButtonHandler.generate_frame(self.screen, 'World Creator', pygame.font.SysFont(MENU_FONT, MENU_FONT_SIZE), (self.screen.get_width() // 2, self.screen.get_height() // 10))
        self.play_button_rect = ButtonHandler.generate_frame(self.screen, 'Play', pygame.font.SysFont(MENU_FONT, MENU_FONT_SIZE), (self.screen.get_width() // 2, self.screen.get_height() * 9 // 10), True)
        self.back_button_rect = ButtonHandler.generate_frame(self.screen, 'Back', self.font, (self.screen.get_width() // 10, self.screen.get_height()  // 10), True)
        
        # options_text_list, rectangles_list = Frames.in_frame_options(self.options_frame, self.options, self.font, self.highlight_states)

        # # Wyświetl zawartość na ekranie
        # for option_text, rect in zip(options_text_list, rectangles_list):
        #     self.screen.blit(option_text[1], rect)
                
        y = 0
        for index, (option, values) in enumerate(self.options.items()):
            y_sum = y + self.options_frame[0] + self.scroll_y
            if y_sum >= self.options_frame[0] and y_sum<= self.options_frame[1] - MENU_OPTIONS_OFFSET // 2:
                text_color = MENU_HIGHLIGHT_COLOR if self.highlight_states[option] else MENU_BASE_COLOR
                text = self.font.render(option, True, text_color)
                rect = text.get_rect(topleft=(MENU_OPTIONS_X, y_sum))
                self.screen.blit(text, rect)
                text_selected = self.font.render(self.selected_options[option], True, text_color)
                rect_selected = text_selected.get_rect(topleft=(WIDTH//2, y_sum))
                self.screen.blit(text_selected, rect_selected)
            y += MENU_OPTIONS_OFFSET // 2

    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            scroll_direction = event.y
            if scroll_direction > 0 and self.scroll_y < 0:  
                self.scroll_y += 10
            elif scroll_direction < 0 and (self.options_frame[0] + MENU_OPTIONS_OFFSET // 2 * (len(self.options) + 1) + self.scroll_y > self.options_frame[1] ):  
                self.scroll_y -= 10
                
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.go_back()
        
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                y = 0
                
                if self.play_button_rect.collidepoint(mouse_pos):
                    # self.game.change_scene('MapGenerator')
                    self.game.change_scene('Gameplay')
                elif self.back_button_rect.collidepoint(mouse_pos):
                    self.go_back()
                else:
                    for key, values in self.options.items():
                        text_rect = self.font.render(key, True, MENU_BASE_COLOR).get_rect(topleft=(MENU_OPTIONS_X, y + self.options_frame[0] + self.scroll_y))
                        
                        if text_rect.collidepoint(mouse_pos):
                            self.change_option(key)
                        y += MENU_OPTIONS_OFFSET // 2
        
        if event.type == MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            y = 0
            for option in self.options:
                text_rect = self.font.render(option, True, MENU_BASE_COLOR).get_rect(topleft=(MENU_OPTIONS_X, y + self.options_frame[0] + self.scroll_y))
                
                if text_rect.collidepoint(mouse_pos):
                    self.highlight_states[option] = True
                else:
                    self.highlight_states[option] = False
                y += MENU_OPTIONS_OFFSET // 2
    
    def change_option(self, key):
        current_index = self.options[key].index(self.selected_options[key])
        next_index = (current_index + 1) % len(self.options[key])
        self.selected_options[key] = self.options[key][next_index]

    def go_back(self):
        self.game.change_scene('MainMenu')
