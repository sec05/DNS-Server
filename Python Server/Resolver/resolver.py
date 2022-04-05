import dns.message
import dns.rdtypes
from Resolver.parser import Parser
def ServeDNS(data: dns.message.Message):
    Parser(data)

