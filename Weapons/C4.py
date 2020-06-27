import pygame
import sys
import os

from Weapon import Weapon
from Types import WeaponType

class C4(Weapon):

    def __init__(self):   #add more args
        super().__init__("C4", 1, 100, 1, WeaponType.c4)