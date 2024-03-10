import pygame
import random
from pygame.locals import *
import sys
from pygame import font
import time

class gridObj:
    def __init__(self, bgColor, playerList, safe, coordinate):
        self.bgColor = bgColor
        self.playerList = playerList
        self.safe = safe
        self.coordinate = coordinate

class Token:
    def __init__(self, Id, color, state, coordinate,size):
        self.Id = Id
        self.color = color
        self.state = state
        self.coordinate = coordinate
        self.size=size
        self.original_coordinate = coordinate
