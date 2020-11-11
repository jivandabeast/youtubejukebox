from queue import Queue
from threading import Thread
import time

def do_stuff(q):
  while True:
    print(q.get())
    time.sleep(2)
    q.task_done()

q = Queue(maxsize=0)
num_threads = 1

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

for x in range(100):
  print("putting in " + str(x))
  q.put(x)

q.join()