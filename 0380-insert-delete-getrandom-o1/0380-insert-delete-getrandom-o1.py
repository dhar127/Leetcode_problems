class RandomizedSet:
    
    def __init__(self):
        self.l=set()

    def insert(self, val: int) -> bool:
        if val not in self.l:
            self.l.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.l:
            self.l.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.l))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()