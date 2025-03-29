"""Use a stack to create a new list with the 
    items in the following list reversed: 
    [1, 2, 3, 4, 5] .  """

class Stack:
    def __init__(self):
        self.items = []

    def is_empty (self):
        return self.items == []
    
    def push (self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
    
    def size(self):
        return len(self.items)
    
stack = Stack()
for num in [1, 2, 3, 4, 5]:
    stack.push(str(num))

reversed = []

for i in range(len(stack.items)):
    reversed += stack.pop()



print(reversed)



