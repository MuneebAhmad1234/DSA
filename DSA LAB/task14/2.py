def lcs_recursive_memoization(X, Y):
    memo = {}

    def helper(i, j):
        if i == 0 or j == 0:
            return ""
        if (i, j) in memo:
            return memo[(i, j)]
        if X[i - 1] == Y[j - 1]:
            memo[(i, j)] = helper(i - 1, j - 1) + X[i - 1]
        else:
            left = helper(i - 1, j)
            right = helper(i, j - 1)
            memo[(i, j)] = left if len(left) > len(right) else right
        return memo[(i, j)]

    return helper(len(X), len(Y))


def lcs_tabulation(X, Y):
    m, n = len(X), len(Y)
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + X[i - 1]
            else:
                dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]

    return dp[m][n]


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"

    print("LCS (Recursive + Memoization):", lcs_recursive_memoization(X, Y))
    print("LCS (Tabulation):", lcs_tabulation(X, Y))
