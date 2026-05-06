import pygame
from settings import *
from dino import *

pygame.init()
clock = pygame.time.Clock()

bg = pygame.image.load(bg_path)
bg = pygame.transform.scale(bg,(screen_width,screen_height))
ground = pygame.image.load(ground_path)
    
dino = Dino()
playerGroup = pygame.sprite.Group()
playerGroup.add(dino)

def moveGround():
    global groundX
    groundX -=groundSpeed
    if groundX < -40:
        groundX = 0


while running:
    clock.tick(60)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   gameOn = not gameOn
                
                if event.key == pygame.K_d and gameOn == True:
                     dino.dinoState = "dead"
                
                if event.key == pygame.K_r and gameOn == True:
                     dino.dinoState = "run"

                if event.key == pygame.K_w and gameOn == True:
                     dino.dinoState = "walk"

                if event.key == pygame.K_i:
                     dino.dinoState = "idle"
                     gameOn = False

                if event.key == pygame.K_j and gameOn == True:
                     dino.dinoState = "jump"
    
    if gameOn:
        moveGround()
    screen.blit(bg,(0,0))
    screen.blit(ground,(groundX,groundY))
    playerGroup.draw(screen)
    playerGroup.update()
    pygame.draw.rect(screen,"red",dino,2)
    pygame.display.update()