import os
import csv
import random
from constants import *

class MapGenerator:
    TERRAIN_PATHS = {
        'Plains': "assets/map_tiles/Plains.png",
        'Forest': "assets/map_tiles/Forest.png",
        'Lake': "assets/map_tiles/Lake.png",
        'Hills': "assets/map_tiles/Hills.png",
        'Clay': "assets/map_tiles/Clay.png"
    }

    CHANCES = {path: (globals()[f'CHANCE_{name.upper()}'], globals()[f'{name.upper()}_ID']) 
               for name, path in TERRAIN_PATHS.items()}
    
    @staticmethod
    def generate_map(size):
        map_size = {'Small': 50, 'Medium': 100, 'Large': 200}[size]
        map_array = [[None for _ in range(map_size)] for _ in range(map_size)]
        
        for y in range(map_size):
            for x in range(map_size):
                terrain_image = random.choices(list(MapGenerator.CHANCES.keys()), 
                                                weights=[chance[0] for chance in MapGenerator.CHANCES.values()])[0]
                terrain_id = MapGenerator.CHANCES[terrain_image][1]
                map_array[y][x] = terrain_id

        return map_array

    @staticmethod
    def save_map(map_data):
        game_num = 1
        game_path = f"data/saved_games/game{game_num}"
        while os.path.exists(game_path):
            game_num += 1
            game_path = f"data/saved_games/game{game_num}"
        os.makedirs(game_path)
        
        with open(os.path.join(game_path, "map.csv"), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(map_data)

# Test
if __name__ == "__main__":
    map_data = MapGenerator.generate_map('Medium')
    MapGenerator.save_map(map_data)