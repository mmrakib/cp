def unique_bsts(n: int):
    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        total = 0

        for j in range(1, i + 1):
            left = dp[j - 1]
            right = dp[i - j]
            total += left * right

        dp[i] = total

    return dp[n]

print(unique_bsts(3))
