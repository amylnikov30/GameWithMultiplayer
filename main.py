import pygame
import sys
import os

from game import Game
from typeEnums import GamemodeType
from player import Player
from position import Position

'''game = Game(1920, 1080)

game.run()'''

p1 = Player("Player1", Position(100, 200), 100, 100)
p2 = Player("Player2", Position(300, 400), 100, 100)




if __name__ == "__main__":
    game = Game(GamemodeType.deathmatch, 42069, p1)
    game.run()