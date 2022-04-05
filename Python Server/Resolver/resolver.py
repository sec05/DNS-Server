from email.policy import default
from soupsieve import match
import dns.message
import dns.rdtypes
def ServeDNS(data: dns.message.Message):
    if(data.question[0].name == dns.rdtype.A):
        
    print(data.question[0].name)
    print(data.question[0].rdclass)
    print(data.question[0].rdtype == dns.rdatatype.A)
    print(data.question[0].covers)
   # print(data.question[0].rdtype == dns.rdtypes.IN.A)
