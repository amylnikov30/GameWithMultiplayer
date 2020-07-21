import pygame
import sys
import os

import socket
import pickle

from player import Player
from network import Network
from game import Game
from server import Server

class Client:

    def __init__(self, game, player):
        self.game = game
        self.player = player


    # def events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             self.quit()
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 self.quit()
    #             if event.key == pygame.K_a:
    #                 self.player.move(dx=-1)
    #             if event.key == pygame.K_d:
    #                 self.player.move(dx=1)
    #             if event.key == pygame.K_w:
    #                 self.player.move(dy=-1)
    #             if event.key == pygame.K_s:
    #                 self.player.move(dy=1)

    def main(self):

        #self.p = self.network.getId()
        self.network = Network()
        self.p = self.network.getId()

        while True:
            self.game.new()
            self.game.run()

game = Game()
player = Player(game, 5, 5)
#server = Server(game)
c = Client(game, player)
#server.run()
c.main()
