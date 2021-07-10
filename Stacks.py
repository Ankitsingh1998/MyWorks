#Data structure - stack
class Stack:
    def __init__(self):
        self.items = []  
  
    def is_empty(self):
        return self.items == []
  
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        print(self.items)

s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()
print('Removed item is:',s.pop())
s.print_stack()
print(s.is_empty())

"""
Stack --> similar to a pile of stack(woods), created by using list.
Last In, First Out --> LIFO, last one inserted is getting at first 
place and whenever we pop/remove an item it will be the first one.
Here, items will store our elements.
push --> adds an item at first place.
pop --> removes an item from first place.
"""
"""
Applications:
    --> can be used to create undo/redo functionalities, parsing
    expressiions (infix to postfix/prefix conversion), and much more.
"""
