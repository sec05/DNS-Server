import dns.message
import dns.rdtypes
def ServeDNS(data: dns.message.Message):
    print(dns.rdtypes.IN.A)
   # print(data.question[0].rdtype == dns.rdtypes.IN.A)
