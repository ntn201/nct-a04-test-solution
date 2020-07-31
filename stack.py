class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        res = ""
        for i in self.items:
            res += str(i) + ' '
        return res[:-1]
    
    def is_empty(self):
        return self.items == []
    
    def push(self,value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def clear(self):
        self.items = []

