from random import random
import dns.resolver
import csv
import time
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['127.0.0.1']
domains = []
data = []
i = 0
with open(r'tests/domains.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        domains.append(row[1])
        i+=1
        if i == 50:
            break
domains.pop(0)
j = 0
c = 0
for j in range(5):
    start = time.time_ns()
    for i in range(100):
        c += 1
        index = int(random() * len(domains)) 
        print(c, domains[index])
        try:
            answer = resolver.resolve(domains[index])
        except:
            continue
        #for rr in answer:
        # print(domains[index] +": "+str(rr))
    end = time.time_ns()
    print("Took "+str((end-start)/(10 ** 9))+" seconds to query random domains!")
    data.append((end-start)/(10 ** 9))


print(data)