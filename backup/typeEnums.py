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
    heavy = 6
    smg = 7



class PlayerType(Enum):
    ct = 1
    t = 2
    legacy = 3


class LegacyPlayers(Enum):  #might have to make it inherit from PlayerType
    Aubery = 1
    Brandon = 2
    Carl = 3
    Charlie = 4
    Dennis = 5
    DonJuan = 6
    Earl = 7
    George = 8
    Graham = 9
    Jacket = 10
    Jake = 11
    Jones = 12
    Louie = 13
    Nigel = 14
    Peter = 15
    Phil = 16
    Rami = 17
    Rasmus = 18
    Richtior = 19
    Rick = 20
    Rufus = 21
    Tony = 22
    Williem = 23
    Zack = 24


class GamemodeType(Enum):
    defuse = 1
    hostage = 2
    deathmatch = 3
    custom = 4


