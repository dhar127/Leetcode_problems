class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        @cache
        def f(i, balance):
            if i==n: return balance==0
            if balance<0: return False
            ans=False
            if s[i]=='(': ans=f(i+1, balance+1)
            elif s[i]==')': ans=f(i+1, balance-1)
            else: ans=f(i+1, balance+1) or f(i+1, balance) or f(i+1, balance-1)
            return ans
        return f(0, 0)