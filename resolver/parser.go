package resolver
import (
	"github.com/miekg/dns"
	//"log"
	"net"
)
func Parser(message *dns.Msg) *dns.A{
 for _, msg := range message.Question{
	 switch msg.Qclass{
	 case dns.TypeA:
			Query(msg)
	 }
 }
 m :=dns.A{
	Hdr: dns.RR_Header{Name: message.Question[0].Name, Rrtype: dns.TypeA, Class: dns.ClassINET, Ttl: 30, },
	A: net.ParseIP("127.0.0.1"),
}
 return &m
}	