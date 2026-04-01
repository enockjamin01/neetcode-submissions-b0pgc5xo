class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dicts={}

    def get(self, key: int) -> int:
        if key in self.dicts.keys():
            val=self.dicts[key]
            del self.dicts[key]
            self.dicts[key]=val
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dicts.keys():
            del self.dicts[key]
            self.dicts[key]=value
        else:
            if len(self.dicts)<self.capacity:
                self.dicts[key]=value
            else:
                del self.dicts[list(self.dicts.keys())[0]]
                self.dicts[key]=value
        


        
