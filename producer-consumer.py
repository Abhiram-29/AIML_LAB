import threading
import time
import random

buffer = []
BUFFER_SIZE = 5
buffer_lock = threading.Condition()

def producer():
    while True:
        item = random.randint(1, 100)
        with buffer_lock:
            while len(buffer) >= BUFFER_SIZE:
                print("Buffer full, producer is waiting.")
                buffer_lock.wait()
            buffer.append(item)
            print(f"Producer produced item: {item}")
            buffer_lock.notify()
        time.sleep(random.uniform(1, 2))

def consumer():
    while True:
        with buffer_lock:
            while not buffer:
                print("Buffer empty, consumer is waiting.")
                buffer_lock.wait()
            item = buffer.pop(0)
            print(f"Consumer consumed item: {item}")
            buffer_lock.notify()
        time.sleep(random.uniform(1, 3))

# Create producer and consumer threads
producers = [threading.Thread(target=producer) for _ in range(2)]
consumers = [threading.Thread(target=consumer) for _ in range(2)]

# Start all threads
for p in producers + consumers:
    p.start()

# Join all threads
for p in producers + consumers:
    p.join()
