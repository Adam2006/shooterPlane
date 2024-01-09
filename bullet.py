import pygame.sprite as s
import math

class Bullet(s.Sprite):
    def __init__(self, pygame, start_pos, target_pos):
        super().__init__()
        self.pygame = pygame
        self.original_image = pygame.image.load("bullet.png")
        self.original_image = pygame.transform.scale(self.original_image, (30, 6))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos
        self.speed = 15
        self.angle = math.atan2(target_pos[1] - self.rect.centery, target_pos[0] - self.rect.centerx)
    def rotate_image(self):
        rotated_image = self.pygame.transform.rotate(self.original_image, math.degrees(-self.angle))
        self.image = rotated_image
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        if self.rect.y<-100:
            self.kill()
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)
        self.rotate_image()
