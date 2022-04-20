import socket
import dns.message
from Resolver.resolver import ServeDNS
class Server:
    def __init__(self, p, n) -> None:
        self.port = p
        ip = n
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((ip,self.port))
    
    def setHandler(self, h) -> None:
        self.handler = h
    
    def run(self) -> None:
        print("Starting DNS server on port "+str(self.port)+"!")
        while True:
            data, addr = self.s.recvfrom(512)
            message = dns.message.from_wire(data)
            self.handler(message, addr)

def main():
    s = Server(53,"")
    s.setHandler(ServeDNS)
    s.run()

if __name__ == "__main__":
    main()






    