import collections
import random
import time

def generate_random_numbers(n):
    max_val = int(input("Enter the maximum value for the random numbers: "))
    return [random.randint(1, max_val) for _ in range(n)]

def linear_search_move_to_front(array, key):
    indexes = []
    for i in range(len(array)):
        if array[i] == key:
            array[i], array[0] = array[0], array[i]
            indexes.append(i)
    return indexes

def calculate_time_complexity(func, *args):
    start_time = time.time_ns()
    result = func(*args)
    end_time = time.time_ns()
    elapsed_time_ns = end_time - start_time
    elapsed_time_s = elapsed_time_ns / 1e9
    return result, elapsed_time_ns, elapsed_time_s

try:
    
    n = int(input("Enter the number of elements to be generated: "))

    
    deq = collections.deque(generate_random_numbers(n))
    print(f"Randomly generated numbers: {list(deq)}")

    
    key = int(input("Enter the maximum number that can be generated: "))

    
    indexes, time_ns, time_s = calculate_time_complexity(linear_search_move_to_front, list(deq), key)

    if indexes:        
        print(f"Time complexity: {time_ns} nanoseconds ({time_s} seconds)")
        print(f"Index/ices found: {indexes}")
    else:
        print("Key not found.")
except ValueError:
    print("Invalid input. Please enter an integer.")
