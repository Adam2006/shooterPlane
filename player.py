import math
import pygame.sprite as s
from bullet import Bullet

class Player(s.Sprite):
    def __init__(self, pygame, game):
        super().__init__()
        self.pygame = pygame
        self.health = 5
        self.original_image = pygame.image.load("player.png")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.original_image = pygame.transform.scale(self.original_image, (75, 75))
        self.rect.center = (game.screenWidth/2, game.screenHeight-100)
        self.speed = 6
        self.shootLevel = 2
        self.points = 0
        self.pointsToUpgrade = {2:3, 3:5, 4:10, 5:"Maxed"}
        self.bullets = pygame.sprite.Group()

    def set_direction(self):
        mouse_x, mouse_y = self.pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)
        self.angle_degrees = math.degrees(angle)
        if (20<-self.angle_degrees<160):
            self.image = self.pygame.transform.rotate(self.original_image, -self.angle_degrees)
            


    def set_movement(self):
        mouse_x, _ = self.pygame.mouse.get_pos()
        self.target_x = mouse_x
        if self.rect.centerx < self.target_x:
            self.rect.centerx += min(self.speed, self.target_x - self.rect.centerx)
        elif self.rect.centerx > self.target_x:
            self.rect.centerx -= min(self.speed, self.rect.centerx - self.target_x)

    def shoot(self):
        if (0<-self.angle_degrees<180):
            top_center_y = self.rect.top + self.rect.height // 2
            top_center_x = self.rect.left + self.rect.width // 2
            mouse_x, mouse_y = self.pygame.mouse.get_pos()
            if(self.shootLevel==1):
                bullet = Bullet(self.pygame, (top_center_x-10,top_center_y), (mouse_x, mouse_y))
                self.bullets.add(bullet)
            elif(self.shootLevel==2):
                bullet = Bullet(self.pygame, (top_center_x,top_center_y), (mouse_x+10, mouse_y))
                self.bullets.add(bullet)
                bullet = Bullet(self.pygame, (top_center_x-20,top_center_y), (mouse_x-10, mouse_y))
                self.bullets.add(bullet)
            elif(self.shootLevel==3):
                bullet = Bullet(self.pygame, (top_center_x,top_center_y), (mouse_x+10, mouse_y))
                self.bullets.add(bullet)
                bullet = Bullet(self.pygame, (top_center_x-20,top_center_y), (mouse_x-10, mouse_y))
                self.bullets.add(bullet)
                bullet = Bullet(self.pygame, (top_center_x-10,top_center_y-10), (mouse_x, mouse_y))
                self.bullets.add(bullet)
            elif(self.shootLevel>=4):
                bullet = Bullet(self.pygame, (top_center_x+5,top_center_y), (mouse_x+15, mouse_y))
                self.bullets.add(bullet)
                bullet = Bullet(self.pygame, (top_center_x-25,top_center_y), (mouse_x-15, mouse_y))
                self.bullets.add(bullet)
                bullet = Bullet(self.pygame, (top_center_x-10,top_center_y-10), (mouse_x, mouse_y))
                self.bullets.add(bullet)
                
                bullet = Bullet(self.pygame, (top_center_x+20,top_center_y-20), (mouse_x+60, mouse_y))
                self.bullets.add(bullet)
                bullet = Bullet(self.pygame, (top_center_x-40,top_center_y-20), (mouse_x-60, mouse_y))
                self.bullets.add(bullet)

    def update(self):
        self.set_direction()
        self.set_movement()
        if self.shootLevel<4:
            if (self.points>=self.pointsToUpgrade[self.shootLevel+1]):
                self.points -= self.pointsToUpgrade[self.shootLevel+1]
                self.shootLevel+=1