import pygame,random
import settings as s
class Decor(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(s.cloudImagePath)
        decorHeight_width = random.randint(10,200)
        self.image = pygame.transform.scale(self.image,(decorHeight_width,decorHeight_width))
        self.rect = self.image.get_rect(center=(s.screen_width+100,random.randint(50,400)))
        
    def update(self):
         self.rect.x -=1
         if self.rect.x <-250:
             self.kill()