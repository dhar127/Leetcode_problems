class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for t in tokens:
            if t.isdigit() or (t[0]=='-' and t[1:].isdigit()):
                l.append(int(t))
            else:
                y=l.pop()
                x=l.pop()
                if t=='+':
                    l.append(x+y)
                elif t=='-':
                    l.append(x-y)
                elif t=='*':
                    l.append(x*y)
                elif t=='/':
                    l.append(int(x/y))
        return l[0]
        