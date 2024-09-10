from twisted.internet import reactor, protocol

class P2PServer(protocol.Protocol):
    def connectionMade(self):
        print(f"Novo peer conectado: {self.transport.getPeer().host}")
        self.transport.write(b'Você está conectado ao servidor P2P!\n')

    def dataReceived(self, data):
        print(f"Dados recebidos: {data.decode()}")

class P2PFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return P2PServer()

def main():
    port = 8000
    reactor.listenTCP(port, P2PFactory())
    print(f"Servidor P2P rodando na porta {port}...")
    reactor.run()

if __name__ == "__main__":
    main()
