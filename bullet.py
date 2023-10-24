import pygame
from helpers import load_png
from constants import NORMAL_VERTICAL_BULLET_SIZE, NORMAL_HORIZONTAL_BULLET_SIZE

class Bullet(pygame.sprite.Sprite):
    """
    A class representing a bullet in a Pygame-based game.

    Attributes:
        images (dict): Dictionary containing bullet images for different directions.
        image (pygame.Surface): The current bullet image.
        rect (pygame.Rect): The bullet's rectangular boundary.
        speed (int): The bullet's movement speed.
        id (int): The identifier of the bullet.
        direction (str): The direction in which the bullet is moving.

    Methods:
        draw(screen):
            Draw the bullet on the screen.

        update(screen):
            Update the bullet's position and draw it on the screen.
    """

    def __init__(self, x, y, direction, id):
        """
        Initialize a Bullet object.

        Args:
            x (int): The initial X-coordinate of the bullet.
            y (int): The initial Y-coordinate of the bullet.
            direction (str): The direction in which the bullet is moving ("up," "down," "left," or "right").
            id (int): The identifier of the bullet.
        """
        super().__init__()
        bullet_type = "shotThin"
        category = "bullets"
        self.images = {
            "up": load_png(f"{bullet_type}_up.png", NORMAL_VERTICAL_BULLET_SIZE, category, bullet_type),
            "down": load_png(f"{bullet_type}_down.png", NORMAL_VERTICAL_BULLET_SIZE, category, bullet_type),
            "left": load_png(f"{bullet_type}_left.png", NORMAL_HORIZONTAL_BULLET_SIZE, category, bullet_type),
            "right": load_png(f"{bullet_type}_right.png", NORMAL_HORIZONTAL_BULLET_SIZE, category, bullet_type),
        }
        self.image, self.rect = self.images[direction]
        self.rect.center = (x, y)
        self.speed = 5
        self.id = id
        self.direction = direction

    def draw(self, screen):
        """
        Draw the bullet on the screen.

        Args:
            screen (pygame.Surface): The Pygame surface on which to draw the bullet.
        """
        screen.blit(self.image, self.rect)

    def update(self, screen):
        """
        Update the bullet's position and draw it on the screen.

        Args:
            screen (pygame.Surface): The Pygame surface on which to draw the bullet.
        """
        if self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed

        self.draw(screen)
