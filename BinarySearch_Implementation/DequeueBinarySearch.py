import time
import random
from collections import deque

def binarySearch(array, key):
    start_time = time.time_ns()
    indices = []
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        value = array[mid]
        output = getMidValues(value)
        print(f"Value at mid index {mid}: {output}")
        if value == key:
            indices.append(mid)
        if value > key:
            high = mid - 1
        else:
            low = mid + 1
    end_time = time.time_ns()
    time_complexity_ns = end_time - start_time
    time_complexity_s = time_complexity_ns / 1_000_000_000
    print(f"Time complexity: {time_complexity_ns} nanoseconds ({time_complexity_s} seconds)")
    if indices:
        print(f"The key was found at index/ices: {indices}")
    else:
        print("The key was not found in the array.")
    return indices

def getMidValues(value:int)->str:
    data = deque()
    data.append(value)
    output = ''
    for _ in range(len(data)):
        output += str(data[_])
    return output


while True:
    try:
        num_numbers = int(input("Enter the number of elements to be generated: "))
        max_number = int(input("Enter the maximum number that can be generated: "))
        array = sorted([random.randint(1, max_number) for _ in range(num_numbers)])
        print(f"Randomly generated numbers: {array}")
        key = int(input("Enter the key to search: "))
        binarySearch(array, key)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
