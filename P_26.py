# FIFO approach
queue = []

queue.append(1)
queue.append(2)
queue.append(3)
print(f"queue after enqueue {queue}") # The queue  [1,2,3]

frontElement= queue[0]
print(f"front element is {frontElement}") #return front(first) element of the queue

popElement= queue.pop(0)
print(f"element dequeued from queue is {popElement}") #dequeued(pop) the first

print(f"queue after dequeue op {queue}") # The queue after dequeue [2,3]

isEmpty = not bool(queue)
print(isEmpty) # False because queue is not empty

print(len(queue))
