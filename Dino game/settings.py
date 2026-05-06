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

deadImages = r"Dino game\png\Dead "
walkImages = r"Dino game\png\Walk "
idleImages = r"Dino game\png\Idle "
jumpImages = r"Dino game\png\Jump "
runImages = r"Dino game\png\Run "