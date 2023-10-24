import pygame
from helpers import load_image, load_png
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, TILE_SIZE, NORMAL_TANK_SIZE

class Environment():
    """
    A class representing the game environment and terrain in a Pygame-based game.

    Attributes:
        tilemap (list): A 2D list representing the tilemap of the game environment.
        size (int): The size of the environment (number of tiles in a row/column).
        image_dict (dict): A dictionary mapping tile IDs to their corresponding images.
        bullet_explosion_images (list): A list of image frames for bullet explosions.
        tank_explosion_images (list): A list of image frames for tank explosions.

    Methods:
        generate_map_tile():
            Generate an empty tilemap for the environment.

        load_terrain():
            Load the terrain images based on the tilemap.

        update(screen):
            Update and render the environment on the game screen.

        generate_tile_map_1():
            Generate a specific tilemap for the game environment.
    """

    def __init__(self):
        """
        Initialize an Environment object.
        """
        self.tilemap = []
        self.size = 0
        self.image_dict = {}
        self.bullet_explosion_images = []
        self.tank_explosion_images = []
        for num in range(5):
            self.bullet_explosion_images.append(tuple(load_png(f"explosion{num + 1}.png", (15, 15), "explosion", "simple_explosion")))
            self.tank_explosion_images.append(tuple(load_png(f"explosion{num + 1}.png", NORMAL_TANK_SIZE, "explosion", "simple_explosion")))

    def generate_map_tile(self):
        """
        Generate an empty tilemap for the environment.
        """
        for y in range(SCREEN_HEIGHT // TILE_SIZE):
            row = []
            for x in range(SCREEN_WIDTH // TILE_SIZE):
                row.append(0)
            self.tilemap.append(row)

    def load_terrain(self):
        """
        Load the terrain images based on the tilemap.
        """
        for row in self.tilemap:
            for tile_id in row:
                # Load the tile image based on the tile_id
                tile_image, _ = load_image(tile_id)
                if not self.image_dict.get(tile_id):
                    self.image_dict[tile_id] = tile_image

    def update(self, screen):
        """
        Update and render the environment on the game screen.

        Args:
            screen (pygame.Surface): The Pygame surface on which to render the environment.
        """
        for y, row in enumerate(self.tilemap):
            for x, tile_id in enumerate(self.tilemap[y]):
                screen.blit(self.image_dict[tile_id], (x * TILE_SIZE, y * TILE_SIZE))

    def generate_tile_map_1(self):
        """
        Generate a specific tilemap for the game environment.
        """
        self.tilemap = [
            [11, 11, 11, 11, 11, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [11, 11, 11, 11, 11, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [11, 11, 11, 11, 11, 11, 9, 1, 1, 1, 1, 1, 1, 3, 0, 0],
            [11, 11, 11, 11, 11, 10, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0],
            [11, 11, 11, 11, 11, 10, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0],
            [11, 11, 11, 11, 11, 10, 0, 1, 1, 1, 7, 1, 1, 7, 1, 1],
            [11, 11, 11, 11, 11, 10, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0],
            [11, 11, 11, 11, 11, 10, 0, 6, 1, 1, 1, 1, 1, 5, 0, 0],
            [11, 11, 11, 11, 11, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    # id ====== tile
    # 0 ====== normal grass
    # 1 ====== horizontal road
    # 2 ====== vertical road
    # 3 ====== roadCorner lower left
    # 4 ====== roadCorner lower right
    # 5 ====== roadCorner upper left
    # 6 ====== roadCorner upper right
    # 7 ====== road crossing
    # 8 ====== road crossing circle
    # 9 ====== road transition west
    # 10 ===== tilegrass transition east
    # 11 ===== tilesand
