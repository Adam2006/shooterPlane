import pygame
import sys

pygame.init()

# Set up display
width, height = 1200, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laser Collision")

# Load images
player_image = pygame.image.load("player.png")
laser_image = pygame.image.load("lazer.png")

# Create masks
player_mask = pygame.mask.from_surface(player_image)
laser_mask = pygame.mask.from_surface(laser_image)

# Set initial positions
player_rect = player_image.get_rect(topleft=(500, 400))
laser_rect = laser_image.get_rect(topleft=(100, 200))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the laser
    laser_rect.x += 1
    laser_rect.y += 1

    # Check for collision
    collision = player_mask.overlap(laser_mask, (laser_rect.x - player_rect.x, laser_rect.y - player_rect.y))

    # Draw everything
    screen.fill((255, 255, 255))
    screen.blit(player_image, player_rect.topleft)
    screen.blit(laser_image, laser_rect.topleft)

    # Draw collision indicator
    if collision:
        pygame.draw.rect(screen, (255, 0, 0), player_rect, 2)
        pygame.draw.rect(screen, (255, 0, 0), laser_rect, 2)

    pygame.display.flip()
    clock.tick(60)
