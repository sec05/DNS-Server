import dns.message
import dns.query

def Query(domain: str, type: int) -> dns.message.Message:
    print("got a query for ", domain, type)
