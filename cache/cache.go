package cache

import (
	"log"
	"reflect"
	"sync"
	"time"

	"github.com/google/go-cmp/cmp"
	"github.com/miekg/dns"
)

type item struct {
	msg *dns.Msg
	ttl time.Time
	used time.Time
}

type Cache struct {
	sync.Mutex
	items map[string]*item
	size int
	ttl time.Duration
}

func New(capacity int) *Cache {
	cache := new(Cache)
	cache.size = capacity
	cache.items = make(map[string]*item)
	return cache
}

func (cache *Cache) Remove(name string){
	cache.Lock()
	delete(cache.items, name)
	cache.Unlock()
}

func (cache *Cache) Add( name string, m *dns.Msg){	
	if cache.size <= 0 || len(cache.items) + 1 > cache.size{
		cache.Remove(cache.LeastRecentlyUsed())
	}
	
	if _, exists := cache.items[name]; !exists{
		cache.Lock()
		cache.items[name] = &item{m.Copy(), time.Now().UTC().Add(cache.ttl), time.Now()}
		cache.Unlock()
	}

}

func (cache *Cache) Contains(any interface{}) bool{
	switch t := any.(type){
	case string:
		if _, exists := cache.items[t]; exists{
			return true
		}
	case *dns.Msg:
		for _, msg := range cache.items {
			if cmp.Equal(t,msg){
				return true
			}
		}
	default:
		return false
	}	
	return false
}

func (cache *Cache) GetItem(name string) *dns.Msg{
	cache.items[name].used = time.Now()
	return cache.items[name].msg
}

func (cache *Cache) LeastRecentlyUsed() string {
	var LRU string
	var tmpTime time.Time
	for name, msg := range cache.items {
		if len(LRU) == 0 {
			LRU = name
			tmpTime = msg.used
			continue
		}
		if msg.used.Before(tmpTime){
			LRU = name
			tmpTime = msg.used
		}
	}
	return LRU
}
func (cache *Cache) FirstInFirstOut() string {
	if len(cache.items) > 0{
		return reflect.ValueOf(cache.items).MapKeys()[0].String()
	} else {
		return ""
	}
	
}