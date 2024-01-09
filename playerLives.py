import pygame
class Lives:
    def __init__(self):
        self.image = pygame.image.load("playerLives/playerLive5.svg")
        self.rect = self.image.get_rect()
        self.rect.topleft=(20,20)
        
    def update(self, health):
        if(health>0):
            self.image = pygame.image.load(f"playerLives/playerLive{health}.svg")
        
            
            