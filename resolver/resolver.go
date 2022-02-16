package resolver

import (
	//"log"
	"github.com/miekg/dns"
)
type Handler struct{}

func (this *Handler) ServeDNS(writer dns.ResponseWriter, request *dns.Msg){
	message := new(dns.Msg)
	message.SetReply(request)
	message.Compress = false //can check for truncation
	switch request.Opcode{
	case dns.OpcodeQuery:
		m := Parser(message)
		message.Answer = append(message.Answer, m)
	}

	writer.WriteMsg(message)
}