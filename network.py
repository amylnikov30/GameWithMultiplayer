import socket
import pickle



class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.server = socket.gethostname(socket.gethostbyname())
        self.server = "192.168.1.180"
        self.port = 65535
        self.addr = (self.server, self.port)
        self.id = self.connect()
        #self.connect()


    def getId(self):
        return self.id


    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
            #return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
