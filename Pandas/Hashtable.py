# ! Hashtable in Python(Is a threadsafe which solve the race condition)

import threading

shared_dict = {'count': 0}
lock = threading.Lock()


def increment_count():
    for _ in range(1000):
        with lock:  # Ensures only one thread modifies at a time
            shared_dict['count'] += 1


threads = []
for _ in range(10):
    thread = threading.Thread(target=increment_count)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(shared_dict['count'])  # Correctly outputs 10,000
