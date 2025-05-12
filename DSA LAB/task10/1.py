import time
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid]> target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def compare_search_algorithms():

    sizes = [1000, 5000, 10000]
    for size in sizes:
        arr = [random.randint(1, size * 10) for _ in range(size)]
        target = random.choice(arr)
        sorted_arr = sorted(arr)

        
        start_time = time.time()
        linear_search(arr, target)
        linear_time = time.time() - start_time

     
        start_time = time.time()
        binary_search(sorted_arr, target)
        binary_time = time.time() - start_time

        print(f"Array Size: {size}")
        print(f"Linear Search Time: {linear_time:.6f} seconds")
        print(f"Binary Search Time: {binary_time:.6f} seconds")
        print("-" * 40)

# Test Cases
if __name__ == "__main__":
    # Example Input & Output
    arr = [10, 23, 45, 70, 11, 15]
    print(linear_search(arr, 45))  # Output: 2

    sorted_arr = [10, 15, 23, 45, 70]
    print(binary_search(sorted_arr, 45))  # Output: 3

    # Performance Comparison
    compare_search_algorithms()