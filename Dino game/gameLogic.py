import pygame
pygame.init()
from dino import Dino
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