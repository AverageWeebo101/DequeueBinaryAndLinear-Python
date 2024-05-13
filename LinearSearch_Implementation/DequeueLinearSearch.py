import collections
import random
import time

def generate_random_numbers(n, max_val):
    return [random.randint(1, max_val) for _ in range(n)]

def linear_search(array, key):
    return [i for i, x in enumerate(array) if x == key]

def calculate_time_complexity(func, *args):
    start_time = time.time_ns()
    result = func(*args)
    end_time = time.time_ns()
    elapsed_time_ns = end_time - start_time
    elapsed_time_s = elapsed_time_ns / 1e9
    return result, elapsed_time_ns, elapsed_time_s

try:
    
    n = int(input("Enter the number of elements to be generated: "))
    max_val = int(input("Enter the maximum number that can be generated: "))

    
    deq = collections.deque(generate_random_numbers(n, max_val))
    print(f"Randomly generated numbers: {list(deq)}")

    
    key = int(input("Enter the key to search: "))

    
    indexes, time_ns, time_s = calculate_time_complexity(linear_search, deq, key)

    if indexes:        
        print(f"Time complexity: {time_ns} nanoseconds ({time_s} seconds)")
        print(f"The key was found at index/ices: {indexes}")
    else:
        print("Key not found.")
except ValueError:
    print("Invalid input. Please enter an integer.")
