import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    res = arr.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
    return res

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

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

data = random.sample(range(1, 10001), 1000)

times = {}

start = time.time()
bubble_sort(data)
times["Bubble Sort"] = time.time() - start

start = time.time()
merge_sort(data)
times["Merge Sort"] = time.time() - start

start = time.time()
quick_sort(data)
times["Quick Sort"] = time.time() - start

print("\nExecution Time Table:")
print("----------------------")
for algo, t in times.items():
    print(f"{algo}: {t:.6f} seconds")

plt.figure(figsize=(10, 6))
plt.bar(times.keys(), times.values(), color=['red', 'blue', 'green'])
plt.title('Execution Time of Sorting Algorithms')
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (seconds)')
plt.grid(axis='y')
plt.show()
