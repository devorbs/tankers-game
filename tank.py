import pygame
from helpers import load_png
from constants import NORMAL_TANK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from bullet import Bullet
from health_bar import HealthBar

class Tank(pygame.sprite.Sprite):
    """
    A class representing a tank in a Pygame-based game.

    Attributes:
        images (dict): Dictionary containing tank images for different directions.
        current_direction (str): The current direction of the tank.
        image (pygame.Surface): The current tank image.
        rect (pygame.Rect): The tank's rectangular boundary.
        speed (int): The tank's movement speed.
        player (int): The player number (1 or 2).
        health (int): The tank's health points.
        lives (int): The number of lives remaining.
        shoot_cooldown (int): The cooldown time between shots in milliseconds.
        last_shot_time (int): The timestamp of the last shot.
        health_bar (HealthBar): The tank's health bar.

    Methods:
        get_health():
            Get the tank's current health.

        initial_vals(x, y, direction):
            Initialize initial position and direction values for the tank.

        reset():
            Reset the tank's position, direction, health, and decrement lives.

        shoot(bullets):
            Fire a bullet from the tank's current position and direction.

        move(direction):
            Move the tank in the specified direction.

        event_handler(bullets):
            Handle user input for tank movement and shooting.

        reduce_health(amount):
            Reduce the tank's health by a specified amount.

        handle_collision(other_tank):
            Handle a collision with another tank, separating them.

        draw(image, screen):
            Draw the tank's image on the screen.

        update(screen, bullets):
            Update the tank's state, handle input, and draw it on the screen.
    """

    def __init__(self, x, y, player, tank_type):
        """
        Initialize a Tank object.

        Args:
            x (int): The initial X-coordinate of the tank.
            y (int): The initial Y-coordinate of the tank.
            player (int): The player number (1 or 2).
            tank_type (str): The type of tank (e.g., "blue" or "red").
        """
        super().__init__()
        category = "tanks"
        self.images = {
            "up": load_png(f"{tank_type}_up.png", NORMAL_TANK_SIZE, category, tank_type),
            "down": load_png(f"{tank_type}_down.png", NORMAL_TANK_SIZE, category, tank_type),
            "left": load_png(f"{tank_type}_left.png", NORMAL_TANK_SIZE, category, tank_type),
            "right": load_png(f"{tank_type}_right.png", NORMAL_TANK_SIZE, category, tank_type),
        }

        if player == 1:
            self.current_direction = "left"
        else:
            self.current_direction = "right"

        self.image, self.rect = self.images[self.current_direction]
        self.rect.center = (x, y)
        self.speed = 3
        self.player = player
        self.health = 50
        self.lives = 3
        self.shoot_cooldown = 250
        self.last_shot_time = 0
        self.health_bar = HealthBar(self, NORMAL_TANK_SIZE[0], 2)

        self.initial_vals(x, y, self.current_direction)

    def get_health(self):
        """
        Get the current health of the tank.

        Returns:
            int: The tank's current health.
        """
        return self.health

    def initial_vals(self, x, y, direction):
        """
        Initialize the initial position and direction values for the tank.

        Args:
            x (int): The initial X-coordinate.
            y (int): The initial Y-coordinate.
            direction (str): The initial direction.
        """
        self.init_x = x
        self.init_y = y
        self.init_direction = direction

    def reset(self):
        """
        Reset the tank's position, direction, health, and decrement lives.
        """
        self.rect.center = (self.init_x, self.init_y)
        self.current_direction = self.init_direction
        self.health = 50
        self.lives -= 1

    def shoot(self, bullets):
        """
        Fire a bullet from the tank's current position and direction.

        Args:
            bullets (list): A list to store the bullets fired by the tank.
        """
        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot_time >= self.shoot_cooldown:
            if self.current_direction == "up":
                x, y = self.rect.midtop
            elif self.current_direction == "down":
                x, y = self.rect.midbottom
            elif self.current_direction == "left":
                x, y = self.rect.midleft
            elif self.current_direction == "right":
                x, y = self.rect.midright

            bullet = Bullet(x, y, self.current_direction, self.player)
            bullets.append(bullet)

            self.last_shot_time = current_time

    def move(self, direction):
        """
        Move the tank in the specified direction.
        Updates the current_direction and image.

        Args:
            direction (str): The direction to move ("up," "down," "left," or "right").
        """
        self.current_direction = direction
        self.image, _ = self.images[direction]

        if direction == "up" and self.rect.y > 0:
            self.rect.y -= self.speed
        if direction == "down" and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
        if direction == "left" and self.rect.x > 0:
            self.rect.x -= self.speed
        if direction == "right" and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def event_handler(self, bullets):
        """
        Handle user input for tank movement and shooting.

        Args:
            bullets (list): A list to store the bullets fired by the tank.
        """
        keys = pygame.key.get_pressed()

        if self.player == 1:
            if keys[pygame.K_UP]:
                self.move("up")
            elif keys[pygame.K_DOWN]:
                self.move("down")
            elif keys[pygame.K_LEFT]:
                self.move("left")
            elif keys[pygame.K_RIGHT]:
                self.move("right")
            if keys[pygame.K_KP_ENTER]:
                self.shoot(bullets)
        if self.player == 2:
            if keys[pygame.K_w]:
                self.move("up")
            elif keys[pygame.K_s]:
                self.move("down")
            elif keys[pygame.K_a]:
                self.move("left")
            elif keys[pygame.K_d]:
                self.move("right")
            if keys[pygame.K_SPACE]:
                self.shoot(bullets)

    def reduce_health(self, amount):
        """
        Reduce the tank's health by a specified amount.

        Args:
            amount (int): The amount by which to reduce the tank's health.
        """
        self.health -= amount

    def handle_collision(self, other_tank):
        """
        Handle a collision with another tank, separating them.

        Args:
            other_tank (Tank): The other tank involved in the collision.
        """
        dx = other_tank.rect.centerx - self.rect.centerx
        dy = other_tank.rect.centery - self.rect.centery

        length = (dx ** 2 + dy ** 2) ** 0.5
        if length == 0:
            length = 1

        dx /= length
        dy /= length

        overlap = (self.rect.width / 2 + other_tank.rect.width / 2) - length

        self.rect.x -= dx * overlap / 2
        self.rect.y -= dy * overlap / 2
        other_tank.rect.x += dx * overlap / 2
        other_tank.rect.y += dy * overlap / 2

    def draw(self, image, screen):
        """
        Draw the tank's image on the screen.

        Args:
            image (tuple): A tuple containing the tank image and its rect.
            screen (pygame.Surface): The Pygame surface on which to draw the image.
        """
        image_rect = image[1]
        image = image[0]
        screen.blit(image, image_rect)

    def update(self, screen, bullets):
        """
        Update the tank's state, handle user input, and draw it on the screen.

        Args:
            screen (pygame.Surface): The Pygame surface on which to draw the tank.
            bullets (list): A list to store the bullets fired by the tank.
        """
        self.event_handler(bullets)
        self.draw((self.image, self.rect), screen)
        self.health_bar.update()
        self.health_bar.draw(screen)
