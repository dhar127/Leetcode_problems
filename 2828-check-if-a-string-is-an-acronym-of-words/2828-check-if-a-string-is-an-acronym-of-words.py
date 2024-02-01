class Solution:
    def isAcronym(self, words: List[str], st: str) -> bool:
        
        s=""
        for i in words:
            s+=i[0]
        return s==st
        
        