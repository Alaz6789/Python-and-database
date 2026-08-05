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

def drawAuthScreen():
      s.screen.fill("WHITE")
      title = s.font.render("DINO GAME", True, "BLACK")
      s.screen.blit(title,(320,100))
      drawButton("Sign in", s.sign_in_button, "RED")
      drawButton("Sign up", s.sign_up_button, "BLACK")

def drawSignInScreen():
      s.screen.fill("WHITE")
      title = s.font.render("DINO GAME", True,"BLACK")
      s.screen.blit(title,(320,180))
      drawButton("Sign IN", s.sign_in_button,"RED")
      drawButton("Sign OUT", s.sign_up_button, "BLACK")

def drawButton(text, rect, color):
      pygame.draw.rect(s.screen, color, rect,)
      buttonText = s.font.render(text, False, "WHITE")
      textRect = buttonText.get_rect(center=rect.center)
      s.screen.blit(buttonText,textRect)

def setScreen(pos):
      if s.current_screen == s.MENUSCREEN:
        if s.start_button.collidepoint(pos):
                s.current_screen = s.GAMESCREEN
        elif s.quit_button.collidepoint(pos):
                s.running = False

      elif s.current_screen == s.AUTHSCREEN:
        if s.sign_in_button.collidepoint(pos):
                s.current_screen = s.SIGNINSCREEN

      elif s.current_screen == s.SIGNINSCREEN:
            if s.userIDinputArea.collidepoint(pos):
                  s.activeInputBox = "userinput"
            elif s.passwordInputArea.collidepoint(pos):
                  s.activeInputBox = "password"
            else:
                  s.activeInputBox = None            
        
def drawInput(rect, active):
      colour = "GREEN" if active else "RED" 
      pygame.draw_rect(s.screen.color.rect)
      renderedText = s.font.render(text, False, "BLACK")
      textRect = renderedText.get_rect(center=rect.center)
      s.screen.blit(renderedText,textRect)
      