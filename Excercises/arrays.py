
class vector:
    """
    mutable array with automatic resizing
    """
    def __init__(self):
        self.container = []
        self.container_capacity = 16
        self.container_len = 0
        self.is_empty = True # make sure to handle case when remove everything from container

    def size(self):
        return len(self.container_len)
    
    def capacity(self):
        return self.container_capacity

    def is_empty(self):
        return self.is_empty
    
    def at(self, index):
        assert(index < self.size() and index > 0)
        return self.container[index]
    
    def resize(self):
        # check to see if we still have space, if not, make some more and update cap
        if self.size() == self.container_capacity:
            # Double capacity
            self.container_capacity *= 2
        if self.size() <= self.container_capacity / 4:
            self.container_capacity /= 2

    def check_and_update_capacity(self):
        self.resize()

    def insert(self, index, item):
        assert(index < self.size() and index > 0)
        self.check_and_update_capacity()

        # copy everything to the next cell
        for i in range(index, self.size()):
            self.container[i+1] = self.container[i]

        # copy the item to its intended cell
        self.container[index] = item
        # update container_len
        self.container_len += 1
    

    def push(self, item):
        # add item to end
        self.insert(self.size(), item)

    def prepend(self, item):
        # add item to beginning
        self.insert(0, item)
    
    def delete(self, index):
        assert(index < self.size() and index > 0)
        self.check_and_update_capacity()
        # copy everything to the prev cell of index, overwritting index
        for i in range(index, self.size() - 1, -1):
            self.container[i] = self.container[i+1]
        self.container_len -= 1
    
    def pop(self):
        item = self.at(self.size())
        self.delete(self.size())
        return item

    def remove(self, item):
        i = 0
        while True:
            if i >= self.size():
                break # no more found
            if self.at(i) == item:
                self.delete(i)
                i = 0
            i += 1
    
    def find(self, item):
        i = 0
        for i in range(0, self.size()):
            if self.at(i) == item:
                return i
        return -1
        

        
