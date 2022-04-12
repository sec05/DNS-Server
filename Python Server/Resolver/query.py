import dns.message
import dns.resolver
import dns.rdatatype
def Query(domain: str) -> dns.message.Message:
    q = dns.message.make_query(domain, dns.rdatatype.A, flags=0)
    r = dns.query.udp(q, "4.2.2.1")
    return r
