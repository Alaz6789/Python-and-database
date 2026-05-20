import pygame

screen_width = 864
screen_height = 836
groundY = 740
screen = pygame.display.set_mode((screen_width, screen_height))

bg_path = r"Dino game\Background\bg.png"
ground_path = r"Dino game\Background\ground.png"

groundX= 0
gameOn = False
groundSpeed = 4
running = True
FPS = 160
clock = pygame.time.Clock()

cactusImage = r"Dino game\obstacles_png\cactus.png"
spikeImage = r"Dino game\obstacles_png\spikes.png"
cloudImagePath = r"Dino game\obstacles_png\cloud_png.png"
listOfObstacle = [cactusImage, spikeImage]
obstacleW = 100
obstacleH = 100

deadImages = r"Dino game\png\Dead "
walkImages = r"Dino game\png\Walk "
idleImages = r"Dino game\png\Idle "
jumpImages = r"Dino game\png\Jump "
runImages = r"Dino game\png\Run "

font = pygame.font.Font(None, 40)
score = 0
lives = 3

decorGroup = pygame.sprite.Group()
spawn_decor = pygame.USEREVENT +1

bg = None
ground = None

count = 0