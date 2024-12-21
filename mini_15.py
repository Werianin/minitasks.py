import threading
import queue
import numpy as np

task_queue = queue.Queue()


def process_matrix(size, value, times):
    matrix = np.fromfunction(lambda i, j: value ** (i + j), (size, size))
    matrix = np.linalg.matrix_power(matrix, times)

    return np.sum(matrix)


class Producer(threading.Thread):
    def __init__(self, n_tasks):
        super().__init__()
        self.n_tasks = n_tasks

    def run(self):
        for i in range(self.n_tasks):
            size = i + 2
            value = i + 1
            times = i + 1
            task = (size, value, times)
            task_queue.put(task)
            print(f"Produced task: {task}")


class Consumer(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            task = task_queue.get()
            if task is None:
                break

            size, value, times = task
            result = process_matrix(size, value, times)
            print(f"Consumed task with result: {result}")
            task_queue.task_done()


n_tasks = 5
n_consumers = 3


producer = Producer(n_tasks)
producer.start()

consumers = [Consumer() for _ in range(n_consumers)]
for consumer in consumers:
    consumer.start()

producer.join()

for _ in range(n_consumers):
    task_queue.put(None)

for consumer in consumers:
    consumer.join()

print("All tasks completed.")
