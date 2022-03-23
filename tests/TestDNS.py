from random import random
import dns.resolver
import csv
import time
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['127.0.0.1']
domains = []
with open(r'tests/domains.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        domains.append(row[1])
domains.pop(0)
start = time.time_ns()
for i in range(len(domains)):
    index = int(random() * len(domains))
    answer = resolver.resolve(domains[index])
    for rr in answer:
        print(domains[index] +": "+str(rr))
    domains.pop(index)
end = time.time_ns()
print("Took "+str((end-start)/(10 ** 9))+" seconds to query the top 499 domains!")
