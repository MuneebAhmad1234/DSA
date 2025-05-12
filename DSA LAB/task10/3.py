import time

# Exponential Search Implementation
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, n - 1))

# Helper Binary Search for Exponential Search
def binary_search(arr, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Fibonacci Search Implementation
def fibonacci_search(arr, target):
    n = len(arr)
    fib2 = 0  # (m-2)'th Fibonacci number
    fib1 = 1  # (m-1)'th Fibonacci number
    fib = fib2 + fib1  # m'th Fibonacci number

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1

# Performance Comparison

def compare_search_methods():
    arr = [2, 4, 8, 16, 32, 64, 128]
    target = 32

    # Exponential Search
    start = time.time()
    exp_result = exponential_search(arr, target)
    exp_time = time.time() - start

    # Fibonacci Search
    start = time.time()
    fib_result = fibonacci_search(arr, target)
    fib_time = time.time() - start

    # Binary Search
    start = time.time()
    bin_result = binary_search(arr, target, 0, len(arr) - 1)
    bin_time = time.time() - start

    print(f"Exponential Search: Index {exp_result}, Time {exp_time:.6f}s")
    print(f"Fibonacci Search: Index {fib_result}, Time {fib_time:.6f}s")
    print(f"Binary Search: Index {bin_result}, Time {bin_time:.6f}s")

# Example Usage
if __name__ == "__main__":
    arr = [2, 4, 8, 16, 32, 64, 128]
    print(exponential_search(arr, 32))  # Output: 4
    print(fibonacci_search(arr, 32))   # Output: 4
    compare_search_methods()