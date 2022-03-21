import dns.resolver
import csv
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['127.0.0.1']
domains = []
with open(r'tests/domains.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        domains.append(row[1])
domains.pop(0)
for domain in domains:
    answer = resolver.resolve(domain)
    for rr in answer:
        print(domain +": "+str(rr))
