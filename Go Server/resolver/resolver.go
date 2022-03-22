package resolver

import (
	//"log"
	"main/cache"
	"net"
	"github.com/miekg/dns"
)
type Handler struct{}
var c *cache.Cache = cache.New(128)

func (handler *Handler) ServeDNS(writer dns.ResponseWriter, request *dns.Msg){
	message := new(dns.Msg)
	message.SetQuestion(request.Question[0].Name, 1)
	message.Compress = false //can check for truncation
	switch request.Opcode{
	case dns.OpcodeQuery:
		if c.Contains(request.Question[0].Name){
			ans := &dns.A {Hdr: dns.RR_Header{Name: request.Question[0].Name, Rrtype: dns.TypeA, Class: dns.ClassINET, Ttl: 60},
			A:   net.ParseIP(c.GetItem(request.Question[0].Name).Answer[0].(*dns.A).A.String()),}
			message.Answer = append(message.Answer, ans)
			break
		}
		m := Parser(message)
		message.Answer = append(message.Answer, m)
		
		c.Add(request.Question[0].Name,message)
	}
	message.SetReply(request)
	writer.WriteMsg(message)
	writer.Close()

}