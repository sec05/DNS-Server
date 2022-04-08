import dns.message
import dns.rdtypes
from Resolver.parser import Parser
def ServeDNS(data: dns.message.Message):
    message = dns.message.Message()
    message.question = data.question
    name = Parser(message)

