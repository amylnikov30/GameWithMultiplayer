import pygame
import sys
import os
from enum import Enum

class GameObjectType(Enum):

    player = 1
    weapon = 2


class WeaponType(Enum):

    rifle = 1
    pistol = 2
    melee = 3
    grenade = 4
    c4 = 5


class PlayerType(Enum):
    ct = 1
    t = 2


class GamemodeType(Enum):
    defuse = 1
    hostage = 2
    deathmatch = 3
    custom = 4


