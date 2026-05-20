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
        self.rect.bottom = s.groundY

    """
    def loadImages(self):
        cactus = pygame.image.load(s.cactusImage)
        cactus = pygame.transform.scale(cactus,(100,50))
        self.obstacleImages.append(cactus)
        mountain = pygame.image.load(s.spikeImage)
        mountain = pygame.transform.scale(mountain,(50,100))
        self.obstacleImages.append(mountain)

    def obstacleOption(self):
        choice = random.randint(1,3)
        if choice == 1:
            self.image = self.obstacleImage[choice]
        elif choice == 2:
            self.image = self.obstacleImages[choice]
    """


    def update(self):
        self.rect.x -= self.move
        if self.rect.x < -5:
            self.kill
        #self.obstacleOption()