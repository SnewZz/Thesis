# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def clear(self):
        del self.queue[:]

    def get(self, i):
        return self.queue[i]
    
    def setter(self, i, v):
        self.queue[i] = v

mask = [False] * 3
t_score = 10000
is_solved = 0
q = Queue()
q.enqueue((mask, t_score, is_solved))
print(q.size())
mask, t_score, is_solved = q.dequeue()
print(mask)
print(sum(mask))
while sum(mask) == 4:
    q_data = q.dequeue()
    if q_data is None: break
    mask, t_score, is_solved = q_data
if is_solved == 2:
    print("youpi")
print((is_solved, mask))
print(q.size())