class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if i==0 and s[i]=='*':
                continue
            elif s[i]=='*':
                st.pop()
            else:
                st.append(s[i])
        return "".join(st)
        