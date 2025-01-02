def stairs(x: int):
    if x == 0 or x == 1 or x == 2:
        return x

    dp = [0] * (x + 1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2 
    
    for i in range(3, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[x]

print(stairs(6))
