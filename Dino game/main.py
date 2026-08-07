import pygame
pygame.init()
import settings as s
from dino import Dino
from obstacles import Obstacles
import gameLogic as g
import screenLogic as sl
import decor as d
import database as db

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
                if event.key == pygame.K_BACKSPACE:
                    if s.activeInputBox == "userinput":
                        s.userInputText = s.userInputText[0:len(s.userInputText)-1]
                    elif s.activeInputBox == "password":
                        s.passwordText = s.passwordText[0:len(s.passwordText)-1]
                else:
                    if s.activeInputBox == "userinput":
                        s.userInputText += event.unicode
                        s.errorOccur = False
                        s.MismatchError = False
                    elif s.activeInputBox == "password":
                        s.passwordText += event.unicode
                        s.errorOccur = False
            if event.type == s.spawn_decor:  
                 s.decorGroup.add(d.Decor())
            if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 sl.setScreen(mouse_pos)

    if pygame.sprite.spritecollide(dino,s.ObstacleGroup,False,pygame.sprite.collide_mask):
         s.lives -= 1
         s.gameOn = False
         if s.lives == 0:
            g.stopGame(dino)
            s.gameOn = False
            db.save_score(s.username,s.score)
            s.lives = 3
            s.game_over_score = s.score
            s.current_screen = s.GAVEOVERSCREEN
            s.score = 0
    
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

    elif s.current_screen == s.SIGNUPSCREEN:
         sl.drawSignUpScreen()

    elif s.current_screen == s.DATASCREEN:
         sl.drawDataScreen()

    elif s.current_screen == s.HIGHESTSCORESCREEN:
         sl.drawHighestScoreScreen()

    elif s.current_screen == s.GAVEOVERSCREEN:
         sl.drawGameOverScreen()

    

    pygame.display.update()

db.dinoDatabase.close()