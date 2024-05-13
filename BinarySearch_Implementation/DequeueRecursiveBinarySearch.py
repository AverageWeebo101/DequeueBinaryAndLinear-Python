import time
import random
from collections import deque

def binarySearchRecursive(array, low, high, key, start_time, indices=[]):
    if high >= low:
        mid = low + (high - low) // 2
        value = array[mid]
        print(f"Value at mid index {mid}: {value}")
        if value == key:
            indices.append(mid)
        if value >= key:
            binarySearchRecursive(array, low, mid - 1, key, start_time, indices)
        if value <= key:
            binarySearchRecursive(array, mid + 1, high, key, start_time, indices)
    return indices


while True:
    try:
        num_numbers = int(input("Enter the number of elements to be generated: "))
        max_number = int(input("Enter the maximum number that can be generated: "))
        array = deque(sorted([random.randint(1, max_number) for _ in range(num_numbers)]))
        print(f"Randomly generated numbers: {list(array)}")
        key = int(input("Enter the key to search: "))
        start_time = time.time_ns()
        indices = binarySearchRecursive(list(array), 0, len(array) - 1, key, start_time)
        end_time = time.time_ns()
        time_complexity_ns = end_time - start_time
        time_complexity_s = time_complexity_ns / 1_000_000_000
        print(f"Time complexity: {time_complexity_ns} nanoseconds ({time_complexity_s:.7f} seconds)")
        if indices:
            print(f"The key was found at indices: {indices}")
        else:
            print("The key was not found in the array.")
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
