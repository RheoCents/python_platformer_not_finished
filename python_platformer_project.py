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
    #background
def get_bg(name):
    image = pygame.image.load(join("borrowed_assets", "Background", name))
    _, _, width, height  = image.get_rect()
    tiles = []

    #loop for bg
    for i in range (Width // width +1):
        for j in range(Height // height+1):
            pos = [i*width, j*height]
            tiles.append(pos)
    return tiles, name

#main function -------------------------------------------
def main(window):
    clock =  pygame.time.Clock()
    background, bg_img = get_bg("Purple.png")
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
