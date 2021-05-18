class Stack:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def __len__(self):
        return len(self.items)
    
    def size(self):
        return len(self)
    
    def print_stack(self):
        print(self.items[::-1])

if __name__ == "__main__":

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())

    stack.print_stack()

    print(len(stack), stack.peek(), stack.size())
