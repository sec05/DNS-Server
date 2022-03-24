from random import random
import dns.resolver
import csv
import time
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['127.0.0.1']
domains = []
i = 0
with open(r'tests/domains.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        domains.append(row[1])
        i+=1
        if i == 50:
            break
domains.pop(0)
start = time.time_ns()
for i in range(1000):
    index = int(random() * len(domains))
    answer = resolver.resolve(domains[index])
    for rr in answer:
        print(domains[index] +": "+str(rr))
end = time.time_ns()
print("Took "+str((end-start)/(10 ** 9))+" seconds to query random domains!")
