import time

def fib_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

def fib_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == "__main__":
    n = 10
    print("Fibonacci using Memoization:", fib_memoization(n))
    print("Fibonacci using Tabulation:", fib_tabulation(n))

    start_time = time.time()
    fib_memoization(n)
    print("Memoization Time:", time.time() - start_time)

    start_time = time.time()
    fib_tabulation(n)
    print("Tabulation Time:", time.time() - start_time)
