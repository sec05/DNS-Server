import dns.message
import dns.rdtypes.IN.A
from Resolver.query import Query 

def Parser(data: dns.message.Message) -> dns.message.Message:
    ip = ""

    for q in data.question:
        print(q.rdtype)
        if q.rdtype == dns.rdtypes.IN.A:
            ip = Query(q.name)

    return ip
