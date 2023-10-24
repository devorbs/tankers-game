import pygame

from constants import SCREEN_WIDTH

class Menu:
    """
    A class representing a menu in a Pygame-based game.

    Attributes:
        options (list): A list of menu options.
        selected_option (int): The index of the currently selected option.
        select_cooldown (int): The cooldown time between option selections in milliseconds.
        last_select_time (int): The timestamp of the last option selection.

    Methods:
        render(screen):
            Render the menu options on the screen.

        handle_input():
            Handle user input to navigate and select menu options.
            Returns:
                str: The action associated with the selected option ("start_game" or "quit").
    """

    def __init__(self):
        """
        Initialize the Menu object.

        Initializes menu options and selection-related attributes.
        """
        self.options = ["Start Game", "Quit"]
        self.selected_option = 0
        self.select_cooldown = 150
        self.last_select_time = 0

    def render(self, screen):
        """
        Render the menu options on the screen.

        Args:
            screen (pygame.Surface): The Pygame surface to render the menu on.
        """
        WHITE = (0, 0, 0)
        SELECTED_COLOR = (255, 0, 0)
        NORMAL_COLOR = WHITE

        font = pygame.font.Font(None, 36)

        for i, option in enumerate(self.options):
            if i == self.selected_option:
                text = font.render(option, True, SELECTED_COLOR)
            else:
                text = font.render(option, True, NORMAL_COLOR)

            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 100 + i * 40))

    def handle_input(self):
        """
        Handle user input to navigate and select menu options.

        Returns:
            str: The action associated with the selected option ("start_game" or "quit").
        """
        current_time = pygame.time.get_ticks()

        if current_time - self.last_select_time >= self.select_cooldown:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.selected_option > 0:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif keys[pygame.K_DOWN] and self.selected_option < len(self.options):
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif keys[pygame.K_RETURN]:  # Enter key
                if self.selected_option == 0:  # Start Game
                    return "start_game"
                elif self.selected_option == 2:  # Quit
                    return "quit"

            self.last_select_time = current_time
