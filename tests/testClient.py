from client import Client

c = Client(('localhost', 23302))
#c.requestAudio(50000)
c.requestKeyboard(20)
#c.requestImage()