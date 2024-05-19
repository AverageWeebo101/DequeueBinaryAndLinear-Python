import random
import time

def generate_sorted_array(size, max_value):
    
    random_numbers = [random.randint(1, max_value) for _ in range(size)]
    
    random_numbers.sort()
    return random_numbers

def ternary_search(array, key):
    left, right = 0, len(array) - 1
    while right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if key == array[mid1]:
            return mid1
        if key == array[mid2]:
            return mid2
        if key < array[mid1]:
            right = mid1 - 1
        elif key > array[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1

def main():
    size = int(input("Enter the number of random elements: "))
    max_value = int(input("Enter the maximum value for random numbers: "))

    
    sorted_array = generate_sorted_array(size, max_value)

    print(f"Randomly generated sorted array: {sorted_array}")

    key = int(input("Enter the key to search: "))

    
    start_time = time.time_ns()
    index = ternary_search(sorted_array, key)
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
