import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
DARKORANGE = (255, 140, 0)
DARKBLUE = (0, 34, 64)

def setMode():
    winfo = pygame.display.Info()
    WIDTH = winfo.current_w
    HEIGHT = winfo.current_h

# game settings
WIDTH = 1920    # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 1080  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 300
TITLE = "Hotline Miami 2020 Rework Pre-alpha testing"
BGCOLOR = DARKGREY

TILESIZE = 40
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 800
WALKING_SPEED = 400
DUCKING_SPEED = 200
PLAYER_MESH = pygame.Rect(0, 0, TILESIZE, TILESIZE)

#Weapon settings
BULLET_VEL = 2000
BULLET_TRAVEL_TIME = 4000   #time in milliseconds
FIRERATE = 100              #place holder until other weapons are implemented
BULLET_DAMAGE = 34         #place holder until other weapons are implemented

FULLSCREEN = pygame.FULLSCREEN

DELTA_T = FPS / 1000
