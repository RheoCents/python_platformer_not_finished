import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

#initialization ----------------------------------------------
pygame.init()
pygame.display.set_caption("Rheo's Platformer")

Bg_color = (255,255,255)
Width, Height =  100, 700
FPS = 60
Player_velocity = 5

#display ---------------------------------------------------
game_screen = pygame.display.set_mode((Width, Height))
