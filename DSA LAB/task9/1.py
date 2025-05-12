import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time

def compare_sorting_algorithms():
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time

# Main function to compare sorting algorithms
def compare_sorting_algorithms():
    input_sizes = [100, 500, 1000, 5000]
    bubble_times = []
    selection_times = []
    insertion_times = []

    for size in input_sizes:
        arr = [i for i in range(size, 0, -1)]  # Worst-case input (reverse sorted)
        bubble_times.append(measure_time(bubble_sort, arr))
        selection_times.append(measure_time(selection_sort, arr))
        insertion_times.append(measure_time(insertion_sort, arr))

    # Plotting the results
    plt.plot(input_sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.plot(input_sizes, selection_times, label='Selection Sort', marker='o')
    plt.plot(input_sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithm Time Complexity Comparison')
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Selection Sort:", selection_sort(arr.copy()))
    print("Insertion Sort:", insertion_sort(arr.copy()))
    compare_sorting_algorithms()