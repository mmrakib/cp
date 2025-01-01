def trib(x: int):
    if x == 0 or x == 1 or x == 2: 
        return 0 
    if x == 3:
        return 1

    dp = [0] * (x + 1)
    dp[1] = 0
    dp[2] = 0
    dp[3] = 1

    for i in range(4, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[x]

print(trib(6))
