import dns.message
import dns.rdtypes
from Resolver.query import Query 

def Parser(data: dns.message.Message) -> dns.message.Message:
    ip = dns.message.Message
    for q in data.question:
        ip = Query(q.name, q.rdtype)

    return ip
