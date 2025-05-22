def hanoi(n, from_peg, temp_peg, to_peg):
    if n == 1:
        print("Move disk 1 from", from_peg, "to", to_peg)
    else:
        hanoi(n - 1, from_peg, to_peg, temp_peg)
        print("Move disk", n, "from", from_peg, "to", to_peg)
        hanoi(n - 1, temp_peg, from_peg, to_peg)
hanoi(3, 'A', 'B', 'C')
#time complexity is O(2ⁿ).