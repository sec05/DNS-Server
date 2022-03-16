import dns.resolver

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['127.0.0.1']
answer = resolver.resolve('amazon.com', 'A')
print('The nameservers are:')
for rr in answer:
    print(rr.target)
