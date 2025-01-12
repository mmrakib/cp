def coin_change_min(coins: list[int], sum: int):
    n = len(coins)

    dp = [sum + 1] * (sum + 1)
    dp[0] = 0

    for i in range(1, sum + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[sum] if dp[sum] != sum + 1 else -1

coins = [9, 6, 5, 1]
sum = 19

print(coin_change_min(coins, sum))
