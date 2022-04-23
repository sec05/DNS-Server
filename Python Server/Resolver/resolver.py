import dns.message
import dns.rdatatype
import dns.rrset
import socket
from Resolver.parser import Parser
from Cache.Cache import Cache
c = Cache(0)
def ServeDNS(data: dns.message.Message, addr):
    
    message = dns.message.Message()
    message.question = data.question
    if c.Contains(message):
          name = c.getItem(data.question[0].name)
    else:
      name = Parser(message)
      c.add(data.question[0].name, name)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("",53))
    name.id = data.id
    try:
      s.sendto(name.to_wire(),addr)
    except Exception as e:
      print(e)
     
