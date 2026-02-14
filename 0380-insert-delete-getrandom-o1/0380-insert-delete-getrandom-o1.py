class RandomizedSet:

    def __init__(self):
        self.data_list = []
        self.index_to_val = {}
    def insert(self, val: int) -> bool:
        if val in self.index_to_val:
            return False
        self.data_list.append(val)
        self.index_to_val[val] = len(self.data_list) - 1
        return True
    def remove(self, val: int) -> bool:
        if val not in self.index_to_val:
            return False
        idx = self.index_to_val[val]
        last_val =self.data_list[-1]
        self.data_list[idx] = last_val
        self.index_to_val[last_val] = idx
        self.data_list.pop()
        del self.index_to_val[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.data_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()