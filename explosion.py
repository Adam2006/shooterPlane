import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        self.image = pygame.image.load("explosion.png")
        self.original_image = self.image.copy()  
        self.rect = self.image.get_rect()
        self.rect.center = target.center
        self.frame_count = 0
        self.size_increment = 2  
        self.alpha_decrement = 5  

    def update(self):
        new_width = self.original_image.get_width() + self.size_increment * self.frame_count
        new_height = self.original_image.get_height() + self.size_increment * self.frame_count

        self.image = pygame.Surface((new_width, new_height), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(self.original_image, (new_width, new_height)), (0, 0))

        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

        alpha_value = max(0, 255 - self.frame_count * self.alpha_decrement)
        self.image.set_alpha(alpha_value)

        self.frame_count += 2

        if alpha_value <= 0:
            self.kill()
