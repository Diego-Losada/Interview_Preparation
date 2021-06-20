class Hash_Table:

    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]


    def get_hash(self, key):
        num = 0
        for char in key:
            num += ord(char)
        return num % self.Max

    def __setitem__(self, key, value):
        #get_hash
        hash = self.get_hash(key)
        self.arr[hash] = value
        #set item to hash

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]        

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
