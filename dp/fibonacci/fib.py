def fib(x):
    if x == 0 or x == 1:
        return x

    dp = [0] * (x + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[x]

print(fib(6))
