import pygame
from dino import Dino
import settings as s

def gameLogic():
    dino.index = 0
    dino.dinoState = "Run"
    if not s.gameOn:
        dino.dinostate = "idle"
    
