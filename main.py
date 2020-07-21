import pygame


from game import Game
from server import Server

game = Game()
server = Server(game)
#server.run()

while True:
    game.new()
    game.run()
