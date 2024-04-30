class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count=collections.defaultdict(int)
        total=0
        count[0]=1
        cur=0
        for idx,c in enumerate(word):
            ci=ord(c)-ord('a')
            cur^=(1<<ci)
            total+=count[cur]
            count[cur]+=1
            for i in range(10):
                delta=cur^(1<<i)
                total+=count[delta]
        return total       