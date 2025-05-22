def tailFactorial(n, accumulator=1):
    # Base case: If n is 0, return the accumulated result
    if n == 0:
        return accumulator

    # Recursive case: Multiply the accumulator by n and decrease n
    return tailFactorial(n - 1, accumulator * n)


# Example usage
n = 5
print(tailFactorial(n))  # Expected output: 120
#The time complexity is O(n), where n is the number for which we calculate the factorial.