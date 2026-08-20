import os
import time
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor


# =========================
# CHANGE THESE VALUES
# =========================

NUM_PROCESSES = 5
THREADS_PER_PROCESS = 5


# =========================
# CPU INFORMATION
# =========================

CPU_COUNT = os.cpu_count()

print(f"Your CPU logical cores: {CPU_COUNT}")
print(f"Processes: {NUM_PROCESSES}")
print(f"Threads per process: {THREADS_PER_PROCESS}")
print(
    f"Total worker threads: "
    f"{NUM_PROCESSES * THREADS_PER_PROCESS}"
)


# =========================
# THREAD WORK
# =========================

def thread_task(thread_id):
    print(
        f"    Thread {thread_id} "
        f"running in Process {os.getpid()}"
    )

    time.sleep(2)

    print(
        f"    Thread {thread_id} "
        f"finished in Process {os.getpid()}"
    )


# =========================
# PROCESS WORK
# =========================

def process_task(process_id):

    print(
        f"\nProcess {process_id} started "
        f"(PID: {os.getpid()})"
    )

    with ThreadPoolExecutor(
        max_workers=THREADS_PER_PROCESS
    ) as executor:

        futures = []

        for thread_id in range(THREADS_PER_PROCESS):
            future = executor.submit(
                thread_task,
                thread_id
            )
            futures.append(future)

        # Wait for all threads
        for future in futures:
            future.result()

    print(
        f"Process {process_id} finished "
        f"(PID: {os.getpid()})"
    )


# =========================
# MAIN
# =========================

if __name__ == "__main__":

    processes = []

    for process_id in range(NUM_PROCESSES):

        process = Process(
            target=process_task,
            args=(process_id,)
        )

        process.start()
        processes.append(process)

    # Wait for all processes
    for process in processes:
        process.join()

    print("\nAll work completed.")