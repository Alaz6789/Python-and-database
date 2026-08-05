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

pygame.time.set_timer(s.spawn_decor, 3000)

while s.running:
    s.clock.tick(s.FPS)
    s.count += 1
    if s.count > 300 and s.gameOn == True:
        obstacle = Obstacles()
        s.ObstacleGroup.add(obstacle)
        s.count = 0
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    s.running = False
            if event.type == pygame.KEYDOWN:
                sl.handleKeyEvent(event, dino)
                if s.activeInputBox == "userinput":
                     if event.key == pygame.K_BACKSPACE:
                          s.userInputText - s.userInputText[0:len(s.userInputText)-1]
                     else:
                          s.userInputText += event.unicode
                          print(s.userInputText)
            if event.type == s.spawn_decor:
                 s.decorGroup.add(d.Decor())
            if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 sl.setScreen(mouse_pos)

    if pygame.sprite.spritecollide(dino,s.ObstacleGroup,False,pygame.sprite.collide_mask):
         g.stopGame(dino)
    
    if s.gameOn:
        g.moveGround()
        s.score += 1
    
    if s.current_screen == s.GAMESCREEN:
        sl.screenHandler()
        playerGroup.draw(s.screen)
        playerGroup.update()
        s.ObstacleGroup.draw(s.screen)
        s.ObstacleGroup.update()
        s.decorGroup.draw(s.screen)
        s.decorGroup.update()

    elif s.current_screen == s.MENUSCREEN:
         sl.drawMenuScreen()

    elif s.current_screen == s.GAVEOVERSCREEN:
         sl.drawGameOverScreen()

    elif s.current_screen == s.AUTHSCREEN:
         sl.drawAuthScreen()

    elif s.current_screen == s.SIGNINSCREEN:
         sl.drawSignInScreen()

    

    pygame.display.update()