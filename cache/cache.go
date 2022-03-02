package cache

import (
	"sync"
	"time"

	"github.com/miekg/dns"
)

type item struct {
	msg *dns.Msg
	ttl time.Time
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

func (cache *Cache) Add(m *dns.Msg, name string){
	if cache.size <= 0 || len(cache.items) + 1 > cache.size{
		return
	}
	cache.Lock()
	if _, exists := cache.items[name]; !exists{
		cache.items[name] = &item{m.Copy(), time.Now().UTC().Add(cache.ttl)}
	}
	cache.Unlock()
}