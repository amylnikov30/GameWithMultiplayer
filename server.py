import socket
from _thread import *
#import threading
import sys
import pickle

from player import Player
from game import Game


class Server:

    def __init__(self, game):
        #self.server = socket.gethostbyname(socket.gethostname())
        self.server = "192.168.1.180"
        self.port = 65535
        self.game = game
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.players = [Player(self.game, 5, 5), Player(self.game, 5, 7)]
        # self.connected = set()
        # self.games = {}
        # self.idCount = 0
        self.bind()

    def handleClient(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected")


        connected = True

        while connected:
            msg = conn.recv(2048)

    def bind(self):
        self.s.bind((self.server, self.port))

        # try:
        #     self.s.bind((self.server, self.port))
        # except socket.error as e:
        #     str(e)


    def run(self):
        self.s.listen(4)
        print("Waiting for connection; Server started")

        while True:
            conn, addr = self.s.accept()
            print("Connected to: ", addr)

            # self.idCount += 1
            #
            # self.p = 0
            # self.gameId = (idCount - 1)//2
            #
            # if idCount % 2 == 1:
            #     self.games[gameId]
            #


            start_new_thread(self.threadedClient, (conn, 0))
            # thread = threading.Thread(target=handleClient, args=(conn, addr))
            # thread.start()
            # print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        self.s.close()


    def threadedClient(self, conn, player):
        conn.send(pickle.dumps(self.players[player]))
        reply = ""
        while True:
            try:
                data = pickle.loads(conn.recv(2048))
                #reply = data.decode("utf-8")
                self.players[player] = data

                if not data:
                    print("Disconnected")
                    break
                else:

                    if player == 1:
                        reply = self.players[0]
                    else:
                        reply = self.players[1]

                    print("Received: ", reply)
                    print("Sending: ", reply)
                conn.sendall(pickle.dumps(reply))

            except:
                break

            conn.close()
            print(f"Connection closed")




    def threadedClient2(self, conn, p, gameId):
        pass

if __name__ == "__main__":
        game = Game()
        server = Server(game)
        server.run()
