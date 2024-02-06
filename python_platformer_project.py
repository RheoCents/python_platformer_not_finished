import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

#initialization ----------------------------------------------
pygame.init()
pygame.display.set_caption("Rheo's Platformer")

Width, Height =  1000, 700
FPS = 60
Player_velocity = 5

#display ---------------------------------------------------
window = pygame.display.set_mode((Width, Height))
   
#player/character
class Player(pygame.sprite.Sprite):
    Color = (255, 0, 0)

    #player init
    def __init__(self,x,y, width,height):
        self.rect = pygame.Rect(x,y, width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0

    #player movement
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def left(self, vel):
        self.x_vel = vel
        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0

    def right(self, vel):
        self.x_vel = -vel
        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0
    
    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, win):
        pygame.draw.rect(win, self.Color, self.rect)

    #background
def get_bg(name):
    image = pygame.image.load(join("borrowed_assets", "Background", name))
    _, _, width, height  = image.get_rect()
    tiles = []

    #loop for bg
    for i in range (Width // width +1):
        for j in range(Height // height+1):
            pos = (i*width, j*height)
            tiles.append(pos)
    return tiles, image

# draw -----------------------------------------
def draw (window, background, bg_img, player):
    for tile in background:
        window.blit(bg_img, tile)

    player.draw(window)

    pygame.display.update()

#main function -------------------------------------------
def main(window):
    clock =  pygame.time.Clock()
    background, bg_img = get_bg("Purple.png")

    player = Player(100,100, 50,50)


    game_on = True
    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                break
        
        draw(window, background, bg_img, player)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
