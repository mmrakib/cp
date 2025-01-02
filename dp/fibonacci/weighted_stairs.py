def weighted_stairs(costs: list):
    n = len(costs)

    dp = [0] * (n + 1)
    dp[0] = costs[0]
    dp[1] = costs[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + costs[i]

    return min(dp[n - 1], dp[n - 2])

print(weighted_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
