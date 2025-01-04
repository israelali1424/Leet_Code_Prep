class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)  # Add to the end
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front
        raise IndexError("Dequeue from an empty queue")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    