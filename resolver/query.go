package resolver

import (
	"log"
	
	"github.com/miekg/dns"
)
func Query(domain *dns.Msg) string{
	//domain.A
	
//client := new(dns.Client)
log.Println("Querying verizon for ", domain.Question[0].Name)

	r, err := dns.Exchange(domain, "4.2.2.1:53")
	log.Println(r.Answer)
	if err == nil && len(r.Answer) != 0{
		log.Println(r.Answer[0].Header().Name)
		return r.Answer[0].Header().Name
	}
	return "127.0.0.1"
}