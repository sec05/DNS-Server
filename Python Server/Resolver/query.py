import dns.message
import dns.resolver
import dns.rdatatype

def Query(domain: str) -> dns.message.Message:
    q = dns.message.make_query(domain, dns.rdatatype.A, flags=0)
    r = dns.query.udp(q, "4.2.2.1")
    
    while len(r.answer) == 0:
        print("looping")
        i = 0
        field = r.additional if len(r.additional) != 0 else r.authority
        for d in field:
            if d.rdtype == dns.rdatatype.A:
                break
            else:
                i += 1
        try:
            r = dns.query.udp(q,field[i].to_rdataset().__getitem__(i).to_text())
        except Exception as e:
            print(e, field)
            return r
    while r.answer[0].rdtype == dns.rdatatype.CNAME:
        q = dns.message.make_query(r.answer[0].to_rdataset().__getitem__(0).to_text(), dns.rdatatype.A, flags=0)
        r = dns.query.udp(q, "4.2.2.1")
        r.answer[0].name = domain
    return r
