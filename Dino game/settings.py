import pygame
import os

screen_width = 864
screen_width2 = 1200
screen_height = 836
screen_height2 = 700
groundY = 740
screen = pygame.display.set_mode((screen_width, screen_height))

DIR = os.path.dirname(__file__)

bg_path = DIR + r"\Background\bg.png"
ground_path = DIR + r"\Background\ground.png"

groundX= 0
gameOn = False
groundSpeed = 4
running = True
FPS = 160
clock = pygame.time.Clock()

cactusImage = DIR + r"\obstacles_png\cactus.png"
spikeImage = DIR + r"\obstacles_png\spikes.png"
cloudImagePath = DIR + r"\obstacles_png\cloud_png.png"
listOfObstacle = [cactusImage, spikeImage]
obstacleW = 100
obstacleH = 100

deadImages = DIR + r"\png\Dead "
walkImages = DIR + r"\png\Walk "
idleImages = DIR + r"\png\Idle "
jumpImages = DIR + r"\png\Jump "
runImages = DIR + r"\png\Run "

font = pygame.font.Font(None, 40)
font.italic = True
font.bold = True
score = 0
lives = 3

ObstacleGroup = pygame.sprite.Group()
decorGroup = pygame.sprite.Group()
spawn_decor = pygame.USEREVENT +1
spawn_obstacle = pygame.USEREVENT + 2
obstacle = None

bg = None
ground = None

count = 0

GAVEOVERSCREEN = "main screen"
AUTHSCREEN = "authentication screen"
GAMESCREEN = "game screen"
MENUSCREEN = "menu screen"
SIGNINSCREEN = "sign in"
SIGNUPSCREEN = "sign up"

current_screen = AUTHSCREEN

start_button = pygame.Rect(300,300,200,70)
quit_button = pygame.Rect(300,400,200,70)
sign_in_button = pygame.Rect(300,300,200,70)
sign_up_button = pygame.Rect(300,400,200,70)
user_ID_button = pygame.Rect(300,300,300,70)
user_password_button = pygame.Rect(300,400,300,70)
enter_button = pygame.Rect(300,500,300,70)
goBack_button = pygame.Rect(700,350,100,200)

userInputText = ""
passwordText = ""
username = ""
password = ""
activeInputBox = None

errorOccur = False
MismatchError = False