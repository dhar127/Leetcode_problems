class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        char_count = Counter(s)
        longest_palindrome_length = 0
        has_odd_count = False
        for count in char_count.values():
            longest_palindrome_length += count // 2 * 2
            if count % 2 == 1:
                has_odd_count = True
        if has_odd_count:
            longest_palindrome_length += 1
        
        return longest_palindrome_length