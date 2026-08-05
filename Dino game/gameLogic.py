import pygame
pygame.init()
from dino import Dino
from obstacles import Obstacles
import settings as s

def gameLogic(dino):
    dino.index = 0
    dino.dinoState = "run"
    if not s.gameOn:
        Dino.dinostate = "idle"
    
def moveGround():
    global groundX
    s.groundX -= s.groundSpeed
    if s.groundX < -40:
        s.groundX = 0

def obstacleLogic():
    count += 1
    if count > 100:
        obstacle = Obstacles()
        global ObstacleGroup
        ObstacleGroup.add(obstacle)

def stopGame(dino):
    s.gameOn = False
    dino.dinostate = "dead"
    s.ObstacleGroup.empty()
    s.decorGroup.empty()