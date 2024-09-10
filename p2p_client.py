from twisted.internet import reactor, protocol

class P2PClient(protocol.Protocol):
    def connectionMade(self):
        print("Conectado ao servidor P2P!")
        self.transport.write(b'Olá, servidor!\n')

    def dataReceived(self, data):
        print(f"Resposta do servidor: {data.decode()}")

class P2PClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return P2PClient()

    def clientConnectionFailed(self, connector, reason):
        print("Falha na conexão com o servidor.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Conexão perdida com o servidor.")
        reactor.stop()

def main():
    host = "localhost"
    port = 8000
    reactor.connectTCP(host, port, P2PClientFactory())
    reactor.run()

if __name__ == "__main__":
    main()
    