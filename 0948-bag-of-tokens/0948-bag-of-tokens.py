class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r,s=0,len(tokens)-1,0
        while l<=r:
            if power>=tokens[l]:
                power-=tokens[l]
                l+=1
                s+=1
            else:
                if power+tokens[r]>=tokens[l] and l!=r and s!=0:
                    power+=tokens[r]
                    r-=1
                    s-=1
                else:
                    break
        return s
            
        