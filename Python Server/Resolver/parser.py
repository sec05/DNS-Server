import dns.message
import dns.rdatatype
from Resolver.query import Query 

def Parser(data: dns.message.Message) -> dns.message.Message:
    ip = dns.message.Message()
    for q in data.question:
        if q.rdtype == dns.rdatatype.A: #https://dnspython.readthedocs.io/en/latest/rdatatype-list.html
            ip = Query(q.name)
    return ip
