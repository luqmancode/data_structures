# Queue: FIFO-First In First Out

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return "queue is empty"

    def queue_size(self):
        return len(self.queue)


queue = Queue()
print(queue.is_empty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Size: ", queue.queue_size())
print("Peek: ", queue.peek())
print("Dequeued: ", queue.dequeue())
print("Dequeued: ", queue.dequeue())
print("Dequeued: ", queue.dequeue())
print("Size: ", queue.queue_size())
print("Peek: ", queue.peek())