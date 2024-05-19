import random
import time
from collections import deque
import math

def generate_sorted_array(size, max_value):
    random_numbers = [random.randint(1, max_value) for _ in range(size)]
    random_numbers.sort()
    return deque(random_numbers)

def jump_search(array, key):
    size = len(array)
    step = int(math.sqrt(size))
    prev = 0
    while array[int(min(step, size) - 1)] < key:
        prev = step
        step += int(math.sqrt(size))
        if prev >= size:
            return -1
    while array[int(prev)] < key:
        prev += 1
        if prev == min(step, size):
            return -1
    if array[int(prev)] == key:
        return int(prev)
    return -1

def main():
    size = int(input("Enter the number of random elements: "))
    max_value = int(input("Enter the maximum value for random numbers: "))

    sorted_array = generate_sorted_array(size, max_value)

    print(f"Randomly generated sorted array: {list(sorted_array)}")

    key = int(input("Enter the key to search: "))

    start_time = time.time_ns()
    index = jump_search(sorted_array, key)
    end_time = time.time_ns()

    elapsed_time_ns = end_time - start_time
    elapsed_time_s = elapsed_time_ns / 1e9

    if index != -1:
        print(f"Key {key} found at index {index}.")
    else:
        print(f"Key {key} not found in the array.")

    print(f"Time complexity: {elapsed_time_ns} nanoseconds ({elapsed_time_s:.6f} seconds)")

if __name__ == "__main__":
    main()
