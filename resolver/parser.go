package resolver
import (
	"github.com/miekg/dns"
	"log"
)
func Parser(message *dns.Msg){
	log.Println("Got a request: ", message.String())
 for _, msg := range message.Question{
	 switch msg.Qclass{
	 case dns.TypeA:
			log.Println("Got a RR request")	 
	 }
 }
}	