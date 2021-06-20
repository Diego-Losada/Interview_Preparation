"""
This is my implementation of Stack in python. Stack is a linear data structure that
uses LIFO (Last in, First out) ordering. The main methods are:
pop()
push(item)
peek()
isempty()
size()
The time complexity for all methods is O(1)
"""

class stack:

    def __init__(self):
        self.items = []
        
    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
