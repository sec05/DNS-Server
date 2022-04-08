import dns.message
import dns.resolver

def Query(domain: str) -> dns.message.Message:
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ["4.2.2.1:53"]
    name = resolver.resolve(domain)
    if len(name) != 0:
        print(name)
