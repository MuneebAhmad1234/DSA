import random
import time

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Performance Comparison
def compare_sorting_algorithms():
    sizes = [1000, 5000, 10000]
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        # Quick Sort Timing
        start_time = time.time()
        quick_sort(arr)
        quick_sort_time = time.time() - start_time
        
        # Merge Sort Timing
        start_time = time.time()
        merge_sort(arr)
        merge_sort_time = time.time() - start_time
        
        print(f"Array Size: {size}")
        print(f"Quick Sort Time: {quick_sort_time:.6f} seconds")
        print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")
        print()

# Example Usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Quick Sort Result:", quick_sort(arr))
    print("Merge Sort Result:", merge_sort(arr))
    print("\nPerformance Comparison:")
    compare_sorting_algorithms()