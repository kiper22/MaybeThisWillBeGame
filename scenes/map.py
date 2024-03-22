import pygame
from pygame.locals import *
from constants import *
from scripts.frames import *

class Map:
    def __init__(self, screen, gameplay):
        self.screen = screen
        self.font = pygame.font.SysFont(MENU_FONT, MENU_FONT_SIZE) 
        self.gameplay = gameplay
        
        self.map_x, self.map_y = 0, 0
        self.prev_pos = (0, 0)
        self.is_dragging = False
        
        TERRAIN_PATHS = [
            (PLAINS_ID, "assets/map_tiles/Plains.png"),
            (FOREST_ID, "assets/map_tiles/Forest.png"),
            (LAKE_ID, "assets/map_tiles/Lake.png"),
            (HILLS_ID, "assets/map_tiles/Hills.png"),
            (CLAY_ID, "assets/map_tiles/Clay.png")
        ]
        
        # MAP
        self.map_path = r'data/saved_games/game1/map.csv'
        with open(self.map_path, 'r') as f:
            self.map_rows = [list(map(int, row.strip().split(','))) for row in f.readlines()]
        
        self.terrain_images = {id_: pygame.image.load(path).convert_alpha() for id_, path in TERRAIN_PATHS}

        self.tile_size = (self.terrain_images[PLAINS_ID].get_width(), self.terrain_images[PLAINS_ID].get_height())
        self.number_tiles = int(0.6 * self.screen.get_width() // self.tile_size[0])
        self.map_display_size = (self.number_tiles * self.tile_size[0], self.number_tiles * self.tile_size[1])
        self.map_display_rect = pygame.Rect((self.screen.get_width() // 20),
                                             self.screen.get_height() // 8,
                                             self.number_tiles * self.tile_size[0], 
                                             self.number_tiles * self.tile_size[1])
        
        self.map_surface = self.map_to_display()
        self.calculate_map_subsurface()
        
        # Minimap

    def map_to_display(self):
        map_surface = pygame.Surface((len(self.map_rows[0]) * self.tile_size[0], len(self.map_rows) * self.tile_size[1]))
        for y, row in enumerate(self.map_rows):
            for x, tile_id in enumerate(row):
                terrain_image = self.terrain_images[tile_id]
                map_surface.blit(terrain_image, (x * self.tile_size[0], y * self.tile_size[1]))
        return map_surface
    
    def calculate_map_subsurface(self):
        self.map_subsurface = self.map_surface.subsurface(pygame.Rect(self.map_x, 
                            self.map_y,
                            self.number_tiles * self.tile_size[0], 
                            self.number_tiles * self.tile_size[1]))
        
    def display(self):
        Frames.big_frame(self.screen, self.map_subsurface, self.map_display_rect.x, self.map_display_rect.y)
        self.screen.blit(self.map_subsurface, (self.map_display_rect.x, self.map_display_rect.y))
        
    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.is_dragging = True
            self.prev_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP:
            self.is_dragging = False
            
        if event.type == MOUSEMOTION:
            if self.is_dragging:
                current_pos = pygame.mouse.get_pos()
                self.map_x += self.prev_pos[0] - current_pos[0]
                self.map_y += self.prev_pos[1] - current_pos[1]
                self.prev_pos = current_pos
                
                self.map_x = min(max(self.map_x, 0), (self.map_surface.get_width() - self.map_display_size[0]))
                self.map_y = min(max(self.map_y, 0), (self.map_surface.get_height() - self.map_display_size[1]))

                self.calculate_map_subsurface()
                self.display()