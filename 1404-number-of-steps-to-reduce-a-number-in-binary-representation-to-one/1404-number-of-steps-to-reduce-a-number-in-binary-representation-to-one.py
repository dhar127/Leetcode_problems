class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        while s != '1':
            if s[-1] == '0':
                s = s[:-1]
            else:
                s = self.addBinary(s, '1')  
            count += 1
        return count
    
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        
        return ''.join(result[::-1])
