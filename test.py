import queue

q = queue.Queue()
q.put("h", 1)
q.put("i")

q.get()
print(q.get())