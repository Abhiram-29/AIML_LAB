import threading
import time
import random

class DiningPhilosophers:
    def __init__(self, num_philosophers=5):
        self.num_philosophers = num_philosophers
        # Create semaphores for each fork
        self.forks = [threading.Semaphore(1) for _ in range(num_philosophers)]
        # Semaphore to limit number of philosophers eating simultaneously
        self.eating = threading.Semaphore(num_philosophers - 1)

    def eat(self, philosopher_id):
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers

        # Limit the number of philosophers who can eat simultaneously
        with self.eating:
            # Acquire both forks
            self.forks[left_fork].acquire()
            print(f'Philosopher {philosopher_id} picked up left fork')
            self.forks[right_fork].acquire()
            print(f'Philosopher {philosopher_id} picked up right fork')

            # Eating
            print(f'Philosopher {philosopher_id} is eating')
            time.sleep(random.randint(1, 3))
            print(f'Philosopher {philosopher_id} finished eating')

            # Release both forks
            self.forks[right_fork].release()
            print(f'Philosopher {philosopher_id} put down right fork')
            self.forks[left_fork].release()
            print(f'Philosopher {philosopher_id} put down left fork')

    def think(self, philosopher_id):
        print(f'Philosopher {philosopher_id} is thinking')
        time.sleep(random.randint(1, 3))

    def dine(self, philosopher_id):
        while True:
            self.think(philosopher_id)
            self.eat(philosopher_id)

def main():
    table = DiningPhilosophers()
    philosophers = []
    for i in range(5):
        philosophers.append(threading.Thread(target=table.dine, args=(i,)))
        philosophers[-1].start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()