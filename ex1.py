def minCoins(N, coins):
    # Base case: If the amount is 0, no coins are needed
    if N == 0:
        return 0

    # Initialize the minimum number of coins as a large number
    min_coins = N  # In the worst case, you would need N coins (1 coin for each)

    # Try every coin in the list
    for coin in coins:
        if N >= coin:
            # Recursively calculate the number of coins for the remaining amount
            coins_needed = 1 + minCoins(N - coin, coins)

            # Update the minimum coins if we found a better solution
            if coins_needed < min_coins:
                min_coins = coins_needed

    return min_coins

# Example usage
coins = [1, 5, 10, 25, 50, 100]
N = 63
print(minCoins(N, coins))  # Expected output: 6 (50 + 10 + 1 + 1 + 1)
#O(2^N) (Exponential)  Recursively explores all possible ways to make change