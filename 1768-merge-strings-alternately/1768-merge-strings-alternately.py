class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=""
        for i in range(min(len(word1),len(word2))):
            l+=(word1[i]+word2[i])
        if len(word1)<len(word2):
            l+=word2[len(l)//2:]
        else:
            l+=word1[len(l)//2:]
        return l
            