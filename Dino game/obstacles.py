import pygame
import random
import settings as s
from dino import Dino
pygame.init()

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obstacleGround = s.groundY+30
        self.move = 5
        self.image = pygame.image.load(random.choice(s.listOfObstacle))
        randomHeightAndWidth = random.randint(-70,70)
        self.image = pygame.transform.scale(self.image,(s.obstacleW+randomHeightAndWidth,s.obstacleH+randomHeightAndWidth))
        self.rect = self.image.get_rect(center =(800,0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = s.groundY

    def update(self):
        if s.gameOn:
            self.rect.x -= self.move
            if self.rect.x < -5:
                self.kill