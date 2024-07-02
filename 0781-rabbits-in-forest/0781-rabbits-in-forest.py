class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.Counter(answers)
        result = 0
        for x in count:
            groups = (count[x] + x) // (x + 1)
            result += groups * (x + 1)
        return result