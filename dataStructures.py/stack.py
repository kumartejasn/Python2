# stacks

class Stack:

    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return f"Stack: {self.items}"
    
s=Stack()
s.push(3)
print(s)
print(s.size())
s.push(5)
print(s.size())
print(s.peek())


#collections 

