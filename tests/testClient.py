from client import Client

c = Client(('localhost', 23302))
#c.requestImage()
#c.requestDisplay()
#c.requestAudio(6000)
c.requestKeyboard(40)