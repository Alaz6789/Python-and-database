import pygame
import settings as s
import gameLogic as g
from dino import Dino
pygame.init()

def screenHandler():
    scoreText = s.font.render(f"SCORE : {s.score}", False, "BLACK", "WHITE")
    livesText = s.font.render(f"LIVES : {s.lives}", False, "BLACK", "WHITE")

    s.screen.blit(s.bg,(0,0))
    s.screen.blit(s.ground,(s.groundX,s.groundY))
    s.screen.blit(scoreText,(10,10))
    s.screen.blit(livesText,(s.screen_width-140, 10))

def handleKeyEvent(event, dino):
    if event.key == pygame.K_SPACE:
                   s.gameOn = not s.gameOn
                   g.gameLogic(dino)
                
    if event.key == pygame.K_d and s.gameOn == True:
        dino.index = 0
        dino.dinoState = "dead"
                    
    if event.key == pygame.K_r and s.gameOn == True:
        dino.index = 0
        dino.dinoState = "run"

    if event.key == pygame.K_i:
        dino.dinoState = "idle"
        s.gameOn = False

    if event.key == pygame.K_j and s.gameOn == True:
        dino.index = 0
        dino.startJump()

def drawGameOverScreen():
      pass

def drawMenuScreen():
      s.screen.fill("WHITE")
      title = s.font.render("DINO GAME", True, "BLACK")
      s.screen.blit(title,(320,100))
      drawButton("START", s.start_button, "RED")
      drawButton("QUIT", s.quit_button, "BLACK")

def drawButton(text, rect, color):
      pygame.draw.rect(s.screen, color, rect,)
      buttonText = s.font.render(text, False, "WHITE")
      textRect = buttonText.get_rect(center=rect.center)
      s.screen.blit(buttonText,textRect)

def setScreen(pos):
      if s.start_button.collidepoint(pos):
            s.current_screen = s.GAMESCREEN
      elif s.quit_button.collidepoint(pos):
            s.running = False
            
