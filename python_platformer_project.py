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
Width, Height =  1000, 700
FPS = 60
Player_velocity = 5

#display ---------------------------------------------------
game_screen = pygame.display.set_mode((Width, Height))


#main function -------------------------------------------
def main(window):
    clock =  pygame.time.Clock()
    game_on = True
    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                break
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(game_screen)
