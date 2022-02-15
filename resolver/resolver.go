package resolver

import (
	//"log"

	"github.com/miekg/dns"
)

func HandleRequest(writer dns.ResponseWriter, request *dns.Msg){
	message := new(dns.Msg)
	message.SetReply(request)
	message.Compress = false //can check for truncation
	switch request.Opcode{
	case dns.OpcodeQuery:
		Parser(message)
	}

	writer.WriteMsg(message)
}