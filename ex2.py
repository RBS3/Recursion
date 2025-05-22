def virusSpread(N, P):
    # Base case: If N is 0 hours, the number of infected computers is just P
    if N == 0:
        return P

    # Recursive case: Each infected computer infects 2 new computers
    return virusSpread(N - 1, P * 2)

# Example usage
P = 1  # Starting with 1 infected computer
N = 5  # Virus spreads for 5 hours
print(virusSpread(N, P))  # Expected output: 32
#The time complexity O(N) (Linear) – Calls itself N times, multiplying by 2 each time.
