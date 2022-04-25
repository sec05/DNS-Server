
from threading import Lock
import time
from dataclasses import dataclass
import dns.message

@dataclass
class Item:
    msg: dns.message.Message
    ttl: int
    used: int

class Cache:
    def __init__(self, n) -> None:
        self.size = n
        self.items = dict()
        self.ttl =  600000
        self.mutex = Lock()
    
    def remove(self, name):
        self.mutex.acquire()
        del self.items[name]
        self.mutex.release()

    def add(self, name, msg):
        if self.size < 0 or len(self.items) > self.size:
            self.remove(self.LastInFirstOut())
        
        if name not in self.items:
            self.mutex.acquire()
            self.items[name] = Item(msg, time.time()+self.ttl, time.time())
            self.mutex.release()
    
    def Contains(self, any):
        if type(any) == str:
            if any in self.items:
                return True
        if type(any) == dns.message.Message:
            for item in self.items:
                if len(self.items[item].msg.question) > 0 and self.items[item].msg.question[0].name == any.question[0].name:
                    return True
        return False

    def getItem(self, name):
        self.items[name].used = time.time()
        return self.items[name].msg
    
    def LeastRecentlyUsed(self):
        lru = ""
        tmpTime = 0
        for item in self.items:
            if len(lru)==0:
                lru = item
                tmpTime = self.items[item].used
            else:
                if self.items[item].used < tmpTime:
                    lru = item
                    tmpTime = self.items[item].used
            
        return lru

    def FirstInFirstOut(self):
        if len(self.items) > 0:
            return list(self.items)[0]
        else:
            return ""
    
    def LastInFirstOut(self):
        if len(self.items) > 0:
            return list(self.items)[len(self.items)-1]
        else:
            return ""



    
