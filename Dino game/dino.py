import pygame
from settings import *

class Dino(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.deadImages = []
         self.walkImages = []
         self.runImages = []
         self.jumpImages = []
         self.idleImages = []
         self.loadImage()
         self.dinoGrund = groundY+30
         self.index = 0
         self.image = self.deadImages[self.index]
         self.rect = self.image.get_rect(center=(100,100))
         self.rect.bottom = self.dinoGrund
         self.wait = 0
         self.dinoState = "idle"
    def loadImage(self):
        for i in range(1,9):
             loadedImage = pygame.image.load(deadImages+f"({i}).png")
             loadedImage= pygame.transform.scale(loadedImage,(200,200))
             self.deadImages.append(loadedImage)
        
        for i in range(1,11):
             loadedImage = pygame.image.load(idleImages+f"({i}).png")
             loadedImage= pygame.transform.scale(loadedImage,(200,200))
             self.idleImages.append(loadedImage)
        
        for i in range(1,13):
             loadedImage = pygame.image.load(jumpImages+f"({i}).png")
             loadedImage= pygame.transform.scale(loadedImage,(200,200))
             self.jumpImages.append(loadedImage)
        
        for i in range(1,9):
             loadedImage = pygame.image.load(runImages+f"({i}).png")
             loadedImage= pygame.transform.scale(loadedImage,(200,200))
             self.runImages.append(loadedImage)

        for i in range(1,11):
             loadedImage = pygame.image.load(walkImages+f"({i}).png")
             loadedImage= pygame.transform.scale(loadedImage,(200,200))
             self.walkImages.append(loadedImage)

    def animationHandler(self, imageType):
        self.wait += 1
        if self.wait > 10:
             self. image = imageType[self.index]
             self.wait = 0
             self.index = (self.index+1) % len(imageType)

    def deadAnimation(self):
        self.animationHandler(self.deadImages)

    def idleAnimation(self):
        self.animationHandler(self.idleImages)

    def jumpAnimation(self):
         self.animationHandler(self.jumpImages)

    def runAnimation(self):
         self.animationHandler(self.runImages)

    def walkAnimation(self):
         self.animationHandler(self.walkImages)

    def update(self):
         if self.dinoState == "dead":
              self.deadAnimation()

         if self.dinoState == "idle":
              self.idleAnimation()

         if self.dinoState == "jump":
              self.jumpAnimation()

         if self.dinoState == "run":
              self.runAnimation()

         if self.dinoState == "walk":
              self.walkAnimation()