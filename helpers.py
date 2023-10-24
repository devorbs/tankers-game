import os
from constants import WHITE
import pygame

pygame.font.init()
FONT = pygame.font.Font(None, 36)

def load_png(name, size, image_cat, image_type):
    """
    Load an image and return the image object.

    Args:
        name (str): The name of the image file.
        size (tuple): The size to which the image should be scaled.
        image_cat (str): The category of the image (e.g., "tilesets").
        image_type (str): The type of the image (e.g., "terrain").

    Returns:
        pygame.Surface: The loaded image.

    Raises:
        SystemExit: If the image cannot be loaded.
    """

    images_folder = os.path.join('assets', image_cat, image_type)
    fullname = os.path.join(images_folder, name)
    try:
        image = pygame.transform.scale(pygame.image.load(fullname), size)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit

    return image, image.get_rect()

def load_image(tile_id):
    """
    Load and return an image based on the tile ID.

    Args:
        tile_id (int): The ID of the tile.

    Returns:
        pygame.Surface: The loaded image corresponding to the tile ID.
    """

    # Mapping of tile IDs to image filenames
    tile_image_mapping = {
        0: "tileGrass1.png",
        1: "tileGrass_roadEast.png",
        2: "tileGrass_roadNorth.png",
        3: "tileGrass_roadCornerLL.png",
        4: "tileGrass_roadCornerLR.png",
        5: "tileGrass_roadCornerUL.png",
        6: "tileGrass_roadCornerUR.png",
        7: "tileGrass_roadCrossing.png",
        8: "tileGrass_roadCrossingRound.png",
        9: "tileGrass_roadTransitionW.png",
        10: "tileGrass_transitionW.png",
        11: "tileSand1.png"
    }

    image_name = tile_image_mapping.get(tile_id, "tileGrass1.png")
    return load_png(image_name, (64, 64), "tilesets", "terrain")

def display_health(health, screen):
    """
    Display the player's health on the screen.

    Args:
        health (int): The player's health value.
        screen (pygame.Surface): The Pygame surface on which to display the health.
    """
    health_text = FONT.render(f"Health: {health}", True, WHITE)
    screen.blit(health_text, (10, 10))

def display_score(score, screen):
    """
    Display the player's score on the screen.

    Args:
        score (int): The player's score value.
        screen (pygame.Surface): The Pygame surface on which to display the score.
    """
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 40))

def display_game_over(screen):
    """
    Display a "GAME OVER" message on the screen.

    Args:
        screen (pygame.Surface): The Pygame surface on which to display the message.
    """
    game_over = "GAME OVER!!"
    game_over_text = FONT.render(game_over, True, WHITE)
    screen.blit(game_over_text, (screen.get_rect().centerx - (len(game_over) * 8), screen.get_rect().centery - 36))

def display_game_over_prompt(screen):
    """
    Display a prompt to restart or exit the game after "GAME OVER."

    Args:
        screen (pygame.Surface): The Pygame surface on which to display the prompt.
    """
    font = pygame.font.Font(None, 25)
    game_over = "Press ENTER to play again or ESC to exit"
    game_over_text = font.render(game_over, True, WHITE)
    screen.blit(game_over_text, (screen.get_rect().centerx - 150, screen.get_rect().centery + 46))
