class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k=[]
        for i in candies:
            k.append((i+extraCandies)>=max(candies))
        return k