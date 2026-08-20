import time
import threading


def task(name):
    print(f"{name} started")

    time.sleep(2)   # Simulate I/O waiting

    print(f"{name} finished")


# -------------------------
# Normal / Sequential
# -------------------------

start = time.perf_counter()

task("Task 1")
task("Task 2")
task("Task 3")

end = time.perf_counter()

print(f"\nSequential time: {end - start:.2f} seconds")


# -------------------------
# Threading
# -------------------------

start = time.perf_counter()

t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))
t3 = threading.Thread(target=task, args=("Task 3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.perf_counter()

print(f"\nThreading time: {end - start:.2f} seconds")