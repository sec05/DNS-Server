package resolver

import (
	"github.com/miekg/dns"
	//"log"
	"net"
)

func Parser(message *dns.Msg) *dns.A {
	var ip string
	for _, msg := range message.Question {
		switch msg.Qclass {
		case dns.TypeA:
			ip = Query(message)
		}
	}

	return &dns.A{
		Hdr: dns.RR_Header{Name: message.Question[0].Name, Rrtype: dns.TypeA, Class: dns.ClassINET, Ttl: 60},
		A:   net.ParseIP(ip),
	}
}
