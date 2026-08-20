import time
from multiprocessing import Process


def calculate(name):
    print(f"{name} started")

    total = 0

    for i in range(50_000_000):
        total += i

    print(f"{name} finished")


if __name__ == "__main__":

    start = time.perf_counter()

    # -------------------------
    # Sequential
    # -------------------------

    calculate("Task 1")
    calculate("Task 2")
    calculate("Task 3")
    calculate("Task 4")

    end = time.perf_counter()

    print(f"\nSequential time: {end - start:.2f} seconds")


    # -------------------------
    # Multiprocessing
    # -------------------------

    start = time.perf_counter()

    p1 = Process(target=calculate, args=("Process 1",))
    p2 = Process(target=calculate, args=("Process 2",))
    p3 = Process(target=calculate, args=("Process 3",))
    p4 = Process(target=calculate, args=("Process 4",))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end = time.perf_counter()

    print(f"\nMultiprocessing time: {end - start:.2f} seconds")