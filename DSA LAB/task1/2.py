import time
from functools import lru_cache

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@lru_cache(maxsize=None)
def fib_memoized(n):
    if n <= 1:
        return n
    return fib_memoized(n-1) + fib_memoized(n-2)

test_values = [10, 20, 30, 40]
execution_times = {
    "Recursive": {},
    "Iterative": {},
    "Memoized": {}
}

for n in test_values:
    start = time.time()
    fib_recursive(n)
    execution_times["Recursive"][n] = time.time() - start

    start = time.time()
    fib_iterative(n)
    execution_times["Iterative"][n] = time.time() - start

    start = time.time()
    fib_memoized(n)
    execution_times["Memoized"][n] = time.time() - start

print("Execution Times (in seconds):")
for method in execution_times:
    for n in execution_times[method]:
        print(f"{method} (n={n}): {execution_times[method][n]:.6f}")
