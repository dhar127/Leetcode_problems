from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def can(w, lc):
            wc = Counter(w)
            for i in wc:
                if wc[i] > lc[i]:
                    return False
            return True
        
        def get(w):
            res = 0
            for c in w:
                res += score[ord(c) - ord('a')]
            return res
        
        lc = Counter(letters)
        
        def backtrack(i):
            if i == len(words):
                return 0
            
            res = backtrack(i + 1)
            
            if can(words[i], lc):
                word_score = get(words[i])
                for c in words[i]:
                    lc[c] -= 1
                
                res = max(res, word_score + backtrack(i + 1))
                
                for c in words[i]:
                    lc[c] += 1
            
            return res
        
        return backtrack(0)