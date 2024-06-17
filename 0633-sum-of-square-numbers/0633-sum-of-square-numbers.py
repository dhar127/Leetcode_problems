class Solution:
    def judgeSquareSum(self,c: int) -> bool:
        if c < 0:
            return False
        for x in range(int(math.sqrt(c)) + 1):
            y = math.sqrt(c - x * x)
            if y == int(y):
                return True
        return False

    