import pygame
import math
from explosion import Explosion
from random import randint
from powerUp import Power

class BonusEnemy(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, game, clone):
        super().__init__()
        start_y = start_y - clone*40
        self.game = game
        self.image = pygame.image.load("airplane.png")
        self.original_image = self.image.copy()
        self.image = pygame.transform.rotate(self.original_image, -90)
        self.rect = self.image.get_rect(center=(start_x, start_y))
        self.speed = 3
        self.angle = 90  # Start at 90 degrees
        self.timing = False
        self.health = 1
        self.radius = 1.3
        self.clone = clone
        self.turned = False
    def update(self):
        
        collisions = pygame.sprite.spritecollide(self, self.game.player.bullets, True)
        for bullet in collisions:
            self.health -= 1
        if self.health<=0:
            self.explosition = Explosion(self.rect)
            self.game.explosions.add(self.explosition)
        
        if self.rect.y >1000 or self.health<=0:
            
            self.kill()
            if randint(1,4)==1:
                power = Power(self.rect)
                self.game.powers.add(power)
            return
        
        if 300>self.rect.y>200 and self.turned==False:
            self.timing = True
            

        if self.timing:
            angular_speed = self.speed / self.radius
            self.angle += angular_speed
            self.image = pygame.transform.rotate(self.original_image, -self.angle)
            self.rect.x += self.speed * math.cos(math.radians(self.angle)) * self.radius
            self.rect.y += self.speed * math.sin(math.radians(self.angle)) * self.radius

            if self.angle >= 450:  # Stop after completing a full circle
                self.timing = False
                self.angle = 90  # Reset the angle
                self.image = pygame.transform.rotate(self.original_image, -self.angle)
                self.turned = True
        else:
            self.rect.y += self.speed
