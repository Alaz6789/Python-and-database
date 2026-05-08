import pygame
import settings as s
from dino import Dino
import gameLogic as g

pygame.init()
clock = pygame.time.Clock()

bg = pygame.image.load(s.bg_path)
bg = pygame.transform.scale(bg,(s.screen_width,s.screen_height))
ground = pygame.image.load(s.ground_path)
    
dino = Dino()
playerGroup = pygame.sprite.Group()
playerGroup.add(dino)

def moveGround():
    global groundX
    s.groundX -= s.groundSpeed
    if s.groundX < -40:
        s.groundX = 0


while s.running:
    clock.tick(s.FPS)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    s.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   s.gameOn = not s.gameOn
                
                if event.key == pygame.K_d and s.gameOn == True:
                     dino.dinoState = "dead"
                
                if event.key == pygame.K_r and s.gameOn == True:
                     dino.dinoState = "run"

                if event.key == pygame.K_w and s.gameOn == True:
                     dino.dinoState = "walk"

                if event.key == pygame.K_i:
                     dino.dinoState = "idle"
                     s.gameOn = False

                if event.key == pygame.K_j and s.gameOn == True:
                     dino.dinoState = "jump"
    
    if s.gameOn:
        moveGround()
    s.screen.blit(bg,(0,0))
    s.screen.blit(ground,(s.groundX,s.groundY))
    playerGroup.draw(s.screen)
    playerGroup.update()
    pygame.draw.rect(s.screen,"red",dino,2)
    pygame.display.update()