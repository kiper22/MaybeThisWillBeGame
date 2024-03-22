import pygame
from pygame.locals import *
from constants import *
from scripts.button_handler import *
# from scripts.frames import *

class MainMenu:
    def __init__(self, screen, game):
        self.screen = screen
        self.font = pygame.font.SysFont(MENU_FONT, MENU_FONT_SIZE) 
        self.game = game
        self.background = pygame.image.load("assets/background/Scenery_Main_Menu.png").convert()
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))

        self.options = ["New Game", "Load Game", "Settings", "Exit"]
        self.highlight_states = {option: False for option in self.options}

    def display(self):
        self.screen.blit(self.background, (0, 0))

        ButtonHandler.generate_frame(self.screen, "Tribal Wars", self.font, (self.screen.get_width() // 2, self.screen.get_height() // 10))

        y = HEIGHT // 2
        for option in self.options:
            text_color = MENU_HIGHLIGHT_COLOR if self.highlight_states[option] else MENU_BASE_COLOR
            text = self.font.render(option, True, text_color)
            rect = text.get_rect(topleft=(MENU_OPTIONS_X, y - len(self.options) / 2 * MENU_OPTIONS_OFFSET))
            self.screen.blit(text, rect)
            y += MENU_OPTIONS_OFFSET

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            y = HEIGHT // 2
            for option in self.options:
                text_rect = self.font.render(option, True, MENU_BASE_COLOR).get_rect(topleft=(MENU_OPTIONS_X, y - len(self.options) / 2 * MENU_OPTIONS_OFFSET))
                
                if text_rect.collidepoint(mouse_pos):
                    self.highlight_states[option] = True
                else:
                    self.highlight_states[option] = False
                y += MENU_OPTIONS_OFFSET
                
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.game.quit_game()
        
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                y = HEIGHT // 2
                for option in self.options:
                    text_rect = self.font.render(option, True, MENU_BASE_COLOR).get_rect(topleft=(MENU_OPTIONS_X, y - len(self.options) / 2 * MENU_OPTIONS_OFFSET))
                    
                    if text_rect.collidepoint(mouse_pos):
                        if option == "New Game":
                            self.game.change_scene("WorldCreator")
                        elif option == "Load Game":
                            self.game.change_scene("LoadGame")
                        elif option == "Game Info":
                            print("Game Info")
                        elif option == "Exit":
                            self.game.quit_game()
                    y += MENU_OPTIONS_OFFSET