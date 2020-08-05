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

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 800
WALKING_SPEED = 400
DUCKING_SPEED = 200
PLAYER_MESH = pygame.Rect(0, 0, TILESIZE, TILESIZE)

BOT_MESH = pygame.Rect(0, 0, TILESIZE, TILESIZE)

#Weapon settings
BULLET_VEL = 4000
BULLET_TRAVEL_TIME = 4000   #time in milliseconds
FIRERATE = 100              #place holder until other weapons are implemented
BULLET_DAMAGE = 34         #place holder until other weapons are implemented

FULLSCREEN = pygame.FULLSCREEN

DELTA_T = FPS / 1000




#item settings
RIFLES = {'weapon_m4a1':'m4a1.png'}
SMG = {'weapon_mp7':'mp7.png'}
PISTOLS = {'weapon_deagle':'deagle.png'}
MELEE = {'knife_karambit':'karambit.png'}
WEAPON_MODELS = {'rifles':RIFLES, 'smg':SMG, 'pistols':PISTOLS, 'melee':MELEE}
BOMB_MODELS = {'weapon_c4':'c4.png'}

ITEM_MODELS = {'weapons':WEAPON_MODELS, 'bomb':BOMB_MODELS}



#graphics

PARTICLES = []
TEXTURES = []
MODELS = []

MODELS = os.path.join(img, 'models')
MASKS = os.path.join(models, 'masks')
TEXTURES = os.path.join(img, 'textures')
DOORS = os.path.join(textures, 'doors')
CURSORS = os.path.join(img, 'cursors')
WEAPONS = os.path.join(models, 'weapons')
