from twisted.protocols.basic import LineOnlyReceiver
from twisted.internet import reactor, protocol
from threading import Thread

receiver = None


class Client(LineOnlyReceiver):
    def connectionMade(self):
        global receiver
        receiver = self

    def connectionLost(self, reason):
        print("Connection lost.")

    def lineReceived(self, line):
        line = line.decode()
        self.factory.update(line)

    def sendMsg(self, msg: str):
        if self is None:
            print("Cannot send message to server. No connection.")
        else:
            msg = msg.encode()
            self.sendLine(msg)

    def disconnect(self):
        self.transport.loseConnection()


class ClientFactory(protocol.ClientFactory):
    protocol = Client

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")

    def update(self, data):
        print(data)


class ReactorThread(Thread):
    def __init__(self, host: str, port: int):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.protocol = Client
        self.factory = ClientFactory()
        self.reactor = reactor

    def run(self):
        self.reactor.connectTCP(self.host, self.port, self.factory)
        self.reactor.run(installSignalHandlers=False)

    def stop(self):
        self.reactor.callFromThread(Client.disconnect, receiver)

    def send(self, msg: str):
        self.reactor.callFromThread(Client.sendMsg, receiver, msg)

    def reconnect(self):
        self.reactor.connectTCP(self.host, self.port, self.factory)
        self.reactor.callFromThread(Client.disconnect, receiver)

def main():
    host = "127.0.0.1"
    port = 1234
    r_thread = ReactorThread(host, port)
    r_thread.start()
    while True:
        cmd = input('::::')
        if cmd == 'reconnect':
            r_thread.reconnect()
        elif cmd == '[e]' :
            r_thread.stop()
        else:
            r_thread.send(cmd)

if __name__ == '__main__':
    main()