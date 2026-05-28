import pygame
pygame.init()
import settings as s
from dino import Dino
from obstacles import Obstacles
import gameLogic as g
import screenLogic as sl
import decor as d

s.bg = pygame.image.load(s.bg_path)
s.bg = pygame.transform.scale(s.bg,(s.screen_width,s.screen_height))
s.ground = pygame.image.load(s.ground_path)
    
dino = Dino()
playerGroup = pygame.sprite.Group()
playerGroup.add(dino)

ObstacleGroup = pygame.sprite.Group()

pygame.time.set_timer(s.spawn_decor, 3000)

while s.running:
    s.clock.tick(s.FPS)
    s.count += 1
    if s.count > 300 and s.gameOn == True:
        obstacle = Obstacles()
        ObstacleGroup.add(obstacle)
        s.count = 0
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    s.running = False
            if event.type == pygame.KEYDOWN:
                sl.handleKeyEvent(event, dino)
            if event.type == s.spawn_decor:
                 s.decorGroup.add(d.Decor())
            if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 sl.setScreen(mouse_pos)
    
    if s.gameOn:
        g.moveGround()
    
    if s.current_screen == s.GAMESCREEN:
        sl.screenHandler()
        playerGroup.draw(s.screen)
        playerGroup.update()
        ObstacleGroup.draw(s.screen)
        ObstacleGroup.update()
        s.decorGroup.draw(s.screen)
        s.decorGroup.update()

    elif s.current_screen == s.MENUSCREEN:
         sl.drawMenuScreen()

    elif s.current_screen == s.GAVEOVERSCREEN:
         sl.drawGameOverScreen()

    

    pygame.display.update()