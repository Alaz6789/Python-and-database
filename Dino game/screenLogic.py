import pygame
import settings as s
import gameLogic as g
import database as d
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
      title = s.font.render("Welcome back!", True,"BLACK")
      s.screen.blit(title,(320,180))
      drawInput(s.user_ID_button,s.activeInputBox == "userinput", s.userInputText)
      drawInput(s.user_password_button,s.activeInputBox == "password", len(s.passwordText)*"*")
      drawButton("Go\nBack",s.goBack_button, "ORANGE")
      drawButton("Enter", s.enter_button, "GREY")
      if s.errorOccur:
            tryagain = s.font.render("Try again! Username or Password has no input", True,"RED")
            s.screen.blit(tryagain,(150,600))
      if s.MismatchError:
            MisMatch = s.font.render("Username or Password is not registered", True,"RED")
            s.screen.blit(MisMatch,(150,600))

def drawSignUpScreen():
      s.screen.fill("WHITE")
      title = s.font.render("Hello new player!", True,"BLACK")
      s.screen.blit(title,(320,180))
      drawInput(s.user_ID_button,s.activeInputBox == "userinput", s.userInputText)
      drawInput(s.user_password_button,s.activeInputBox == "password", s.passwordText)
      drawButton("Go \n Back",s.goBack_button, "ORANGE")
      drawButton("Enter", s.enter_button, "GREY")
      if s.errorOccur:
            tryagain = s.font.render("Try again! Username or Password has no input", True,"RED")
            s.screen.blit(tryagain,(300,600))

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
            elif s.sign_up_button.collidepoint(pos):
                s.current_screen = s.SIGNUPSCREEN

      elif s.current_screen == s.SIGNINSCREEN:
            if s.user_ID_button.collidepoint(pos):
                  s.activeInputBox = "userinput"
            elif s.user_password_button.collidepoint(pos):
                  s.activeInputBox = "password"
            elif s.enter_button.collidepoint(pos):
                  if s.userInputText == "" or s.passwordText == "":
                        s.errorOccur = True
                  else:
                        s.username = s.userInputText
                        s.password = s.passwordText
                        s.userInputText = ""
                        s.passwordText = ""
                        d.sign_in(s.username, s.password)
                        if s.MismatchError == False:
                              s.current_screen = s.GAMESCREEN
            elif s.goBack_button.collidepoint(pos):
                  s.current_screen = s.AUTHSCREEN
            else:
                  s.activeInputBox = None            

      elif s.current_screen == s.SIGNUPSCREEN:
            if s.user_ID_button.collidepoint(pos):
                  s.activeInputBox = "userinput"
            elif s.user_password_button.collidepoint(pos):
                  s.activeInputBox = "password"
            elif s.enter_button.collidepoint(pos):
                  if s.userInputText == "" or s.passwordText == "":
                        s.errorOccur = True
                  else:
                        s.username = s.userInputText
                        s.password = s.passwordText
                        s.userInputText = ""
                        s.passwordText = ""
                        d.sign_up(s.username, s.password)
                        s.current_screen = s.AUTHSCREEN
            elif s.goBack_button.collidepoint(pos):
                  s.current_screen = s.AUTHSCREEN
            else:
                  s.activeInputBox = None 
      
def drawInput(rect, active,text):
      color = "GREEN" if active else "RED" 
      pygame.draw.rect(s.screen,color,rect)
      renderedText = s.font.render(text, False, "BLACK")
      textRect = renderedText.get_rect(center=rect.center)
      s.screen.blit(renderedText,textRect)
      