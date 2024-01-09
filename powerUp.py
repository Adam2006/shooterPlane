import pygame
class Power(pygame.sprite.Sprite):
    def __init__(self, targetRect):
        super().__init__()
        self.image = pygame.image.load("powerUp.png")
        self.rect = self.image.get_rect()
        self.rect.center = (targetRect.centerx, targetRect.centery)
    def update(self):
        self.rect.y += 2
        if self.rect.y >1000:
            self.kill()