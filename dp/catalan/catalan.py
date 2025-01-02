def catalan(n: int):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = 0

        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[n]

print(catalan(6))

