class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if not stack or char != brackets[stack.pop()]:
                    return False
        return len(stack) == 0
