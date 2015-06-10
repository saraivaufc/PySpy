from client import Client

c = Client(('localhost', 23302))
c.listServer()
c.requestImage()