class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # To keep track of visited numbers
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return n == 1
