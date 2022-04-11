import dns.message
import dns.rdatatype
import dns.rrset
from Resolver.parser import Parser
def ServeDNS(data: dns.message.Message):
    message = dns.message.Message()
    message.question = data.question
    name = Parser(message)
    message.make_response(name)
    print(message, name)

