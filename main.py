import pygame
from pygame.locals import *
from scenes.main_menu import MainMenu
from scenes.world_creator import WorldCreator
from scenes.load_game import LoadGame
from scenes.gameplay import Gameplay
from constants import *

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.current_scene = MainMenu(self.screen, self)
        self.cursor = pygame.mouse.set_visible(False)
        self.running = True
        
        self.cursor_image = pygame.image.load("assets/icons/Cursor.png").convert_alpha()
        self.cursor_rect = self.cursor_image.get_rect()

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

                self.current_scene.handle_event(event)

            self.screen.fill((255, 255, 255))
            self.current_scene.display()
            
            self.draw_cursor()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def draw_cursor(self):
        self.cursor_rect.topleft = pygame.mouse.get_pos()
        self.screen.blit(self.cursor_image, self.cursor_rect)
    
    def change_scene(self, scene_name):
        scene_class = globals().get(scene_name)
        if scene_class:
            self.current_scene = scene_class(self.screen, self)
        else:
            print(f"Error: Scene '{scene_name}' not found.")
    
    def quit_game(self):
        self.running = False

if __name__ == "__main__":
    game = Main()
    game.start()
