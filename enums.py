import pygame
from enum import Enum



class Direction(Enum):
    x = 1
    y = 2


class WeaponType(Enum):
    rifle = 1
    smg = 2
    pistol = 3
    melee = 4
