package resolver

import (
	"log"
	"reflect"
	"github.com/miekg/dns"
)
func Query(domain *dns.Msg) string{
	r, err := dns.Exchange(domain, "4.2.2.1:53")
	if err == nil && len(r.Answer) != 0{
		tmpR := r
		//log.Println(tmpR)
		for reflect.TypeOf(tmpR.Answer[0]).String() =="*dns.CNAME"{
			domain := new(dns.Msg)
			domain.SetQuestion(tmpR.Answer[0].(*dns.CNAME).Target,1)
		
			r, err := dns.Exchange(domain, "4.2.2.1:53")
			if err != nil{
				log.Println(err.Error(), domain.Question)
				return ""
			}
			tmpR = r
		}
		return tmpR.Answer[0].(*dns.A).A.String()
	}
	return "127.0.0.1"
}