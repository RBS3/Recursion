def pascal(n, k):
    if k == 0 or k == n:
        return 1
    return pascal(n - 1, k - 1) + pascal(n - 1, k)

def print_pascal(n):
    for i in range(n + 1):
        print([pascal(i, k) for k in range(i + 1)])

print_pascal(5)
#Time complexity:O(2 n )