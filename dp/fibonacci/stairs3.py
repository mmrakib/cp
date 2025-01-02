def stairs3(x: int):
    if x == 0 or x == 1 or x == 2:
        return x
    if x == 3:
        return 4

    dp = [0] * (x + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[x]

print(stairs3(6))

