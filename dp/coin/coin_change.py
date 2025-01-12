def coin_change(coins: list, sum: int):
    n = len(coins)

    if n == 0 or sum == 0:
        return 0
    
    dp = [0] * (sum + 1)
    dp[0] = 1
    
    for i in range(n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]

    return dp[sum]

coins = [1, 2, 3]
sum = 5

print(coin_change(coins, sum))
