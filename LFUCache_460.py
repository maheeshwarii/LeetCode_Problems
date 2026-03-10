from collections import defaultdict
from collections import OrderedDict
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.key_to_freq = {}
        self.freq_to_key = defaultdict(OrderedDict)
        self.min_freq = 0

    def update(self, key):
        freq = self.key_to_freq[key]
        del self.freq_to_key[freq][key]
        if not self.freq_to_key[freq]:
            del self.freq_to_key[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_to_freq[key] = freq+1
        self.freq_to_key[freq+1][key] = None

    def get(self, key): 
        if key not in self.cache: return -1
        self.update(key)
        return self.cache[key]
    
    def put(self, key, value):
        if self.capacity==0: return
        if key in self.cache:
            self.cache[key] = value
            self.update(key)
            return
        if len(self.cache)>=self.capacity:
            lfu, _ = self.freq_to_key[self.min_freq].popitem(last=False)
            del self.cache[lfu]
            del self.key_to_freq[lfu]
        self.cache[key] = value
        self.key_to_freq[key] = 1
        self.min_freq = 1
        self.freq_to_key[1][key] = None
        return


#main
n = int(input("Number of instructions:"))
capacity = int(input("Enter capacity:"))
lru = LFUCache(capacity)
for i in range(n):
    parts = input("Enter function:").split()
    if parts[0]=='put':
        key=int(parts[1])
        val=int(parts[2])
        lru.put(key,val)
    elif parts[0]=='get':
        key=int(parts[1])
        print(lru.get(key))