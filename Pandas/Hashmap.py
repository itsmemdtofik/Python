# ! Hashmap in Python (NOT a threadsafe)

import threading
import time

shared_dict = {
    'count': 0
}


def increment_count():
    for _ in range(10000):
        # Simulate a race condition by reading, modifying, and writing back
        current_value = shared_dict['count']

        time.sleep(0.001)
        current_value += 1
        shared_dict['count'] = current_value


# Create a multiple threads to increment the count
threads = []
for _ in range(10):
    thread = threading.Thread(target=increment_count)
    threads.append(thread)
    thread.start()

# wait for all threads to finish
for thread in threads:
    thread.join()

print(shared_dict['count'])  # Expected 10000 but likely less due to race condition

'''
#* Two thread incrementing the same count or running concurrently.
#* Two Thread read count = 0, both increment to 1, and write back to 1(lossing one increment) loosing one increment.
'''
