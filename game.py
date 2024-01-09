import pygame
from sys import exit
from player import Player
from playerLives import Lives
from enemy import Enemy
from bonusEnemy import BonusEnemy
from weaponLevel import WeaponLevelText
from random import randint
pygame.init()

class Game():
    def __init__(self):
        self.screenWidth, self.screenHeight = 1200, 800
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption("Airplane Game")
        self.clock = pygame.time.Clock()
        self.FPS = 80

        self.player = Player(pygame, self)
        self.playerLives = Lives()
        self.enemyGroup = pygame.sprite.Group()
        self.bonusEnemyGroup = pygame.sprite.Group()
        self.enemyBullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        font = pygame.font.Font(None, 36)
        self.weaponLevelText = WeaponLevelText(font, f"Level {self.player.shootLevel}", (self.screenWidth-220 , 40))
        self.pointsText = WeaponLevelText(font, f"Points {self.player.points}", (self.screenWidth-220 , 70))
        self.powers = pygame.sprite.Group()
        self.update()
        

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.shoot()

    def handle_collisions(self):
        collisions_player = pygame.sprite.spritecollide(self.player, self.enemyBullets, True)
        collisions_power = pygame.sprite.spritecollide(self.player, self.powers, True)

        if collisions_power:
            self.player.points += 1
        if collisions_player:
            self.player.health -= 1
            self.playerLives.update(self.player.health)
            if self.player.health <= 0:exit()

    def update_sprites(self):
        self.player.update()
        self.player.bullets.update()
        self.enemyBullets.update()
        self.explosions.update()
        self.enemyGroup.update()
        self.bonusEnemyGroup.update()
        self.powers.update()
        self.weaponLevelText.update(f"Weapon Level : {self.player.shootLevel}")
        msg = f"Points : {self.player.points}/{self.player.pointsToUpgrade[self.player.shootLevel+1]}" if self.player.shootLevel<4 else f"{self.player.pointsToUpgrade[self.player.shootLevel+1]}" 
        self.pointsText.update(msg)
        
        

    def draw_sprites(self):
        self.screen.blit(self.player.image, self.player.rect.topleft)
        self.screen.blit(self.playerLives.image, self.playerLives.rect.topleft)
        self.player.bullets.draw(self.screen)
        self.enemyBullets.draw(self.screen)
        self.enemyGroup.draw(self.screen)
        self.explosions.draw(self.screen)
        self.powers.draw(self.screen)
        self.bonusEnemyGroup.draw(self.screen)
        self.screen.blit(self.weaponLevelText.image, self.weaponLevelText.rect.topleft)
        self.screen.blit(self.pointsText.image, self.pointsText.rect.center)
        

    def update(self):

        counter = 0
        airPlaneCounter = 0
        r = randint(400, 700)
        while True:
            counter += 1
            airPlaneCounter += 1
            
            if counter > 100:

                self.enemyGroup.add(Enemy(self, [self.player.rect.x, self.player.rect.y]))
                counter = 0
            if airPlaneCounter>=r:
                self.bonusEnemyGroup.add(BonusEnemy(400,10, self, 0))
                self.bonusEnemyGroup.add(BonusEnemy(400,10, self, 1))
                self.bonusEnemyGroup.add(BonusEnemy(400,10, self, 2))
                self.bonusEnemyGroup.add(BonusEnemy(400,10, self, 3))
                self.bonusEnemyGroup.add(BonusEnemy(400,10, self, 4))
                r = randint(400, 700)
                airPlaneCounter=0
            self.handle_events()

            self.screen.fill((117, 169, 245))
            

            self.handle_collisions()
            self.update_sprites()
            self.draw_sprites()
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(self.FPS)
