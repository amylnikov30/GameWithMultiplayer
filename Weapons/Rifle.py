import pygame
import sys
import os


from Weapon import Weapon
from Types import WeaponType

class Rifle(Weapon):

    def __init__(self, name, ammo, damage, firerate):    #add more args
        self.name = name
        self.ammo = ammo
        self.damage = damage
        self.firerate = firerate


        super().__init__(self.name, self.ammo, self.damage, self.firerate, WeaponType.rifle)