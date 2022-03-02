package resolver

import (
	//"log"

	"github.com/miekg/dns"
)
type Handler struct{}

func (handler *Handler) ServeDNS(writer dns.ResponseWriter, request *dns.Msg){
	message := new(dns.Msg)
	message.SetQuestion(request.Question[0].Name, 1)
	message.Compress = false //can check for truncation
	switch request.Opcode{
	case dns.OpcodeQuery:
		m := Parser(message)
		message.Answer = append(message.Answer, m)
	}
	message.SetReply(request)
	writer.WriteMsg(message)
	writer.Close()

}