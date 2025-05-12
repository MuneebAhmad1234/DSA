import math
import time

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size
    prev = 0

    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev
    return -1

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + ((x - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def compare_search_methods():
    arr = [i for i in range(1, 10001)]  # Large sorted array
    x = 6789  # Element to search

    start = time.time()
    jump_result = jump_search(arr, x)
    jump_time = time.time() - start

    start = time.time()
    interpolation_result = interpolation_search(arr, x)
    interpolation_time = time.time() - start

    start = time.time()
    binary_result = binary_search(arr, x)
    binary_time = time.time() - start

    print(f"Jump Search: Index {jump_result}, Time {jump_time:.6f} seconds")
    print(f"Interpolation Search: Index {interpolation_result}, Time {interpolation_time:.6f} seconds")
    print(f"Binary Search: Index {binary_result}, Time {binary_time:.6f} seconds")

def explain_search_methods():
    print("\nBest Use Cases:")
    print("1. Jump Search: Best for sorted arrays when random access is efficient (e.g., arrays in memory).")
    print("2. Interpolation Search: Best for uniformly distributed sorted data, as it predicts the position of the target.")
    print("3. Binary Search: General-purpose search for sorted arrays, works well in most cases.")

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    print(jump_search(arr, 7))  # Output: 3
    print(interpolation_search(arr, 7))  # Output: 3

    compare_search_methods()
    explain_search_methods()
