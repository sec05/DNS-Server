package resolver

import (
	//"log"
	
	"github.com/miekg/dns"
)
func Query(domain *dns.Msg) string{
	r, err := dns.Exchange(domain, "4.2.2.1:53")
	if err == nil && len(r.Answer) != 0{
		return r.Answer[0].(*dns.A).A.String()
	}
	return "127.0.0.1"
}