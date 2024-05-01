class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        x=""
        h=0
        for i in word:
            if i==ch:
                x+=i
                break
            else:
                x+=i
            h+=1
        x=x[::-1]+word[1+h:]
        return x
        