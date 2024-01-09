from random import randint
import pygame, math
from enemyBullet import EnemyBullet
from powerUp import Power
from explosion import Explosion
class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, target):
        super().__init__()
        self.game = game
        self.health = 3
        self.speed = 3
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,game.screenWidth)
        self.rect.y = -50
        self.counter = 0        
        self.target = target
        self.angle = math.atan2(target[1] - self.rect.centery, target[0] - self.rect.centerx)
        self.angle_degrees = math.degrees(self.angle)
        self.image = pygame.transform.rotate(self.image, -self.angle_degrees)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.flash_timer = 0
        
        self.rand = randint(50, 100)
        self.original_image = self.image
        
    
    def flash(self):
        if self.flash_timer > 0:
            if pygame.time.get_ticks() % 500 < 250:  # 250 milliseconds for each state
                self.image = self.original_image
            else:
                self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            self.flash_timer -= 1
        else:
            self.image = self.original_image
    
    def update(self):
        collisions = pygame.sprite.spritecollide(self, self.game.player.bullets, True)
        for bullet in collisions:
            self.health -= 1
            self.flash_timer = 10  # Set the flash timer
        if self.health<=0:
            self.explosition = Explosion(self.rect)
            self.game.explosions.add(self.explosition)
        
        if self.rect.y >1000 or self.health<=0:
            
            self.kill()
            if randint(1,3)==1:
                power = Power(self.rect)
                self.game.powers.add(power)
            return
        self.counter+=1
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)
        if(self.counter>self.rand) and self.rect.y+200<self.game.player.rect.y:
            top_center_y = self.rect.top + self.rect.height // 2
            top_center_x = self.rect.left + self.rect.width // 2
            bullet = EnemyBullet(pygame, (top_center_x,top_center_y), self.target)
            self.game.enemyBullets.add(bullet)
            self.counter = 0
        #self.flash()
         

            