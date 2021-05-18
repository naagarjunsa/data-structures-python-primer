class Queue:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def __len__(self):
        return len(self.items)

    def enqueue(self, val):
        self.items.insert(0, val)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def print_queue(self):
        print(self.items)
    
    def size(self):
        return len(self)
    
if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())

    queue.print_queue()

    print(len(queue), queue.size())

