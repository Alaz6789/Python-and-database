import pygame
import os

screen_width = 864
screen_height = 836
groundY = 740
screen = pygame.display.set_mode((screen_width, screen_height))

DIR = os.path.dirname(__file__)

bg_path = os.path.join(DIR,r"Dino game\Background\bg.png")
ground_path = os.path.join(DIR,r"Dino game\Background\ground.png")

groundX= 0
gameOn = False
groundSpeed = 4
running = True
FPS = 160
clock = pygame.time.Clock()

cactusImage = os.path.join(DIR,r"Dino game\obstacles_png\cactus.png")
spikeImage = os.path.join(DIR,r"Dino game\obstacles_png\spikes.png")
cloudImagePath = os.path.join(DIR,r"Dino game\obstacles_png\cloud_png.png")
listOfObstacle = [cactusImage, spikeImage]
obstacleW = 100
obstacleH = 100

deadImages = os.path.join(DIR,r"Dino game\png\Dead ")
walkImages = os.path.join(DIR,r"Dino game\png\Walk ")
idleImages = os.path.join(DIR,r"Dino game\png\Idle ")
jumpImages = os.path.join(DIR,r"Dino game\png\Jump ")
runImages = os.path.join(DIR,r"Dino game\png\Run ")

font = pygame.font.Font(None, 40)
font.italic = True
font.bold = True
font.underline = True
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
SIGNINSCREEN = "sign up"
SIGNUPSCREEN = "sign up"

current_screen = AUTHSCREEN

start_button = pygame.Rect(300,300,200,70)
quit_button = pygame.Rect(300,400,200,70)
sign_in_button = pygame.Rect(300,300,200,70)
sign_up_button = pygame.Rect(300,400,200,70)
user_ID_button = pygame.Rect(300,300,300,70)
user_password_button = pygame.Rect(300,400,300,70)

userInputText = ""
activeInputBox = None