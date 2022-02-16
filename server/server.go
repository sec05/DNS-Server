package server

import (
	"github.com/miekg/dns"
	"strconv"
	"log"
	"main/resolver"
)
//This file needs to init the server, cache, and resolver
func Run(){
	dns.HandleFunc("resolver", resolver.HandleRequest)
	port := 533
	server := &dns.Server{Addr: ":"+strconv.Itoa(port), Net: "udp"}
	log.Printf("Starting DNS server on port %d!",port)
	err := server.ListenAndServe()
	defer server.Shutdown()
	if err != nil{
		log.Fatalf("Error failed to start server: %s",err.Error())
	}
}