import pygame
import settings as s

class Dino(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.deadImages = []
         self.walkImages = []
         self.runImages = []
         self.jumpImages = []
         self.idleImages = []
         self.loadImage()
         self.dinoGround = s.groundY+30
         self.index = 0
         self.image = self.deadImages[self.index]
         self.rect = self.image.get_rect(center=(100,100))
         self.rect.bottom = self.dinoGround
         self.wait = 0
         self.vel = 0
         self.jumpPower = -20
         self.dinoOnGround = True
         self.gravity = 0.8
         self.dinoState = "idle"
    def loadImage(self):
        for i in range(1,9):
             loadedImage = pygame.image.load(s.deadImages+f"({i}).png")
             loadedImage= pygame.transform.scale(loadedImage,(200,200))
             self.deadImages.append(loadedImage)
        
        for i in range(1,11):
             loadedImage = pygame.image.load(s.idleImages+f"({i}).png")
             loadedImage= pygame.transform.scale(loadedImage,(200,200))
             self.idleImages.append(loadedImage)
        
        for i in range(1,13):
             loadedImage = pygame.image.load(s.jumpImages+f"({i}).png")
             loadedImage= pygame.transform.scale(loadedImage,(200,200))
             self.jumpImages.append(loadedImage)
        
        for i in range(1,9):
             loadedImage = pygame.image.load(s.runImages+f"({i}).png")
             loadedImage= pygame.transform.scale(loadedImage,(200,200))
             self.runImages.append(loadedImage)

        for i in range(1,11):
             loadedImage = pygame.image.load(s.walkImages+f"({i}).png")
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
         self.image = self.jumpImages[self.index]
         self.handleGravity()

    def runAnimation(self):
         self.animationHandler(self.runImages)

    def handleGravity(self):
         self.rect.y += self.vel
         self.vel += self.gravity
         if self.rect.bottom >= self.dinoGround:
               self.vel = 0
               self.dinoOnGround = True
               self.rect.bottom = self.dinoGround
               self.dinoState = "run"

    def startJump(self):
         if self.dinoOnGround == True:
              self.vel = self.jumpPower
              self.dinoState = "jump"
              self.dinoOnGround = False
    

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