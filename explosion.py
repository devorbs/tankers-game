import pygame
from helpers import load_png

class Explosion(pygame.sprite.Sprite):
    """
    A class representing an explosion animation in a Pygame-based game.

    Attributes:
        images (list): A list of image frames for the explosion animation.
        index (int): The current frame index for the explosion animation.
        image (pygame.Surface): The current frame image.
        rect (pygame.Rect): The rectangular boundary for the explosion animation.
        finished (bool): Indicates whether the explosion animation is finished.
        animation_speed (int): The speed at which the animation frames change.
        animation_counter (int): A counter for managing animation frame changes.

    Methods:
        update():
            Update the explosion animation by changing frames.

        draw(screen):
            Draw the current frame of the explosion animation on the screen.
    """

    def __init__(self, x, y, width, height, images):
        """
        Initialize an Explosion object.

        Args:
            x (int): The X-coordinate of the explosion.
            y (int): The Y-coordinate of the explosion.
            width (int): The width of the explosion animation frame.
            height (int): The height of the explosion animation frame.
            images (list): A list of image frames for the explosion animation.
        """
        super().__init__()
        self.images = images
        self.index = 0
        self.image = self.images[self.index][0]
        self.rect = self.images[self.index][1]
        self.rect.center = (x, y)
        self.finished = False
        self.animation_speed = 8
        self.animation_counter = 0

    def update(self):
        """
        Update the explosion animation by changing frames.
        """
        if not self.finished:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.index += 1
                if self.index >= len(self.images):
                    self.finished = True
                else:
                    self.image = self.images[self.index][0]
                self.animation_counter = 0

    def draw(self, screen):
        """
        Draw the current frame of the explosion animation on the screen.

        Args:
            screen (pygame.Surface): The Pygame surface on which to draw the explosion animation.
        """
        if not self.finished:
            screen.blit(self.image, self.rect)
