class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f=[]
        g=set(arr)
        for i in g:
            f.append(arr.count(i))
        return len(f)==len(set(f))
        