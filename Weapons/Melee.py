import pygame
import sys
import os

from Weapon import Weapon
from Types import WeaponType

class Melee(Weapon):


    def __init__(self, name, firerate):   #add more args
        self.name = name
        self.firerate


        super().__init__(self.name, 0, 100, self.firerate, WeaponType.melee)



