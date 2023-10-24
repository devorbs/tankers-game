import pygame
import sys

from constants import *
from tank import Tank
from menu import Menu
from environment import Environment
from explosion import Explosion

pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tankers")
clock = pygame.time.Clock()

# Create sprite groups for tanks and bullets
tank_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# Initialize player tanks
tank_player_1 = Tank(SCREEN_WIDTH - (50 + NORMAL_TANK_SIZE[0]), SCREEN_HEIGHT // 2, 1, TANK_TYPE_BLUE)
tank_player_2 = Tank(50, SCREEN_HEIGHT // 2, 2, TANK_TYPE_BLUE)
tank_group.add(tank_player_1, tank_player_2)

# Initialize lists for bullets and explosions
bullets = []
explosions = []

# Create game menu and game environment
menu = Menu()
environment = Environment()
environment.generate_tile_map_1()
environment.load_terrain()
menu_visible = True

# Main game loop
game_running = True
while game_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    screen.fill(WHITE)
    environment.update(screen)
    
    if menu_visible:
        menu.render(screen)
        result = menu.handle_input()
        if result == "start_game":
            menu_visible = False
    else:
        # Update and render tank groups
        tank_group.update(screen, bullets)
        
        # Update and check for collisions with bullets
        for bullet in bullets:
            bullet.update(screen)
            if (
                bullet.rect.left < 0
                or bullet.rect.right > SCREEN_WIDTH
                or bullet.rect.top < 0
                or bullet.rect.bottom > SCREEN_HEIGHT
            ):
                bullets.remove(bullet)
                
            for bullet2 in bullets:
                if bullet != bullet2:
                    if bullet.rect.colliderect(bullet2.rect):
                        if bullet in bullets and bullet2 in bullets:
                            bullets.remove(bullet)
                            bullets.remove(bullet2)
                            explosion1 = Explosion(bullet.rect.centerx, bullet.rect.centery, 15, 15, environment.bullet_explosion_images)
                            explosion2 = Explosion(bullet2.rect.centerx, bullet2.rect.centery, 15, 15, environment.bullet_explosion_images)
                            explosions.append(explosion1)
                            explosions.append(explosion2)
            
            for tank in tank_group:
                if bullet.rect.colliderect(tank.rect) and bullet.id != tank.player:
                    if bullet in bullets:
                        bullets.remove(bullet)
                        explosion = Explosion(bullet.rect.centerx, bullet.rect.centery, 15, 15, environment.bullet_explosion_images)
                        explosions.append(explosion)
                        tank.reduce_health(10)

                    if tank.get_health() < 10:
                        explosion2 = Explosion(tank.rect.centerx, tank.rect.centery, NORMAL_TANK_SIZE[0], NORMAL_TANK_SIZE[1], environment.tank_explosion_images)
                        explosions.append(explosion2)
                        tank.reset()

                    if tank.lives < 1:
                        for tank in tank_group:
                            tank.reset()
                            tank.lives = 3
                        explosions.clear()
                        bullets.clear()
                        menu_visible = True
        
        # Handle tank-to-tank collisions
        for tank_player_1 in tank_group:
            for tank_player_2 in tank_group:
                if tank_player_1 != tank_player_2:
                    if tank_player_1.rect.colliderect(tank_player_2.rect):
                        tank_player_1.handle_collision(tank_player_2)
        
        # Update and draw explosions
        for explosion in explosions:
            explosion.update()
            explosion.draw(screen)
        
        # Remove finished explosions
        explosions = [explosion for explosion in explosions if not explosion.finished]
    
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
