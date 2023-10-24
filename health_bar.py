import pygame
from constants import GREEN, RED

class HealthBar(pygame.sprite.Sprite):
    """
    A class representing a health bar for a tank in a Pygame-based game.

    Attributes:
        tank (Tank): The tank to which the health bar is attached.
        width (int): The width of the health bar.
        height (int): The height of the health bar.
        image (pygame.Surface): The surface on which the health bar is drawn.
        rect (pygame.Rect): The rectangular area of the health bar.
        max_health (int): The maximum health of the tank.
        current_health (int): The current health of the tank.

    Methods:
        update():
            Update the health bar based on the tank's current health.

        draw(screen):
            Draw the health bar on the given screen.
    """

    def __init__(self, tank, width, height):
        """
        Initialize a HealthBar object.

        Args:
            tank (Tank): The tank to which the health bar is attached.
            width (int): The width of the health bar.
            height (int): The height of the health bar.
        """
        super().__init__()
        self.tank = tank
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.midtop = (self.tank.rect.centerx, self.tank.rect.top - 10)
        self.max_health = tank.health
        self.current_health = tank.health

    def update(self):
        """
        Update the health bar based on the tank's current health.
        """
        self.current_health = self.tank.health
        self.rect.midtop = (self.tank.rect.centerx, self.tank.rect.top - 10)
        bar_width = (self.current_health / self.max_health) * self.width
        self.image.fill(GREEN)
        pygame.draw.rect(self.image, RED, (0, 0, self.width, self.height), 2)
        pygame.draw.rect(self.image, GREEN, (0, 0, bar_width, self.height))

    def draw(self, screen):
        """
        Draw the health bar on the given screen.

        Args:
            screen (pygame.Surface): The Pygame surface on which to draw the health bar.
        """
        screen.blit(self.image, self.rect)
