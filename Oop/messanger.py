class MessageBox:

    def __init__(self):
        self.lista = []

    def send(self):
        self.lista.append(2)

    def receive(self):
        self.lista.append(1)

mb = MessageBox()
mb1 = MessageBox()
mb.receive()
mb1.send()
mb.send()
mb.send()
mb1.receive()
mb.receive()
mb.receive()
mb.send()

print(mb.lista, mb1.lista)
# [2, 2, 1, 1, 2]