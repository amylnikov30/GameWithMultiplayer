import pygame
import sys
import os

from Types import WeaponType


class Weapon:

    def __init__(self, name, ammo, damage, firerate, type):  #add more args
        self.name = name
        self.ammo = ammo
        self.damage = damage
        self.firerate = firerate
        self.type = type