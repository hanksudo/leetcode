# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] != s[high]:
                return self.check(s, low + 1, high) or self.check(s, low, high - 1)
            low += 1
            high -= 1

        return True

    def check(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True


assert Solution().validPalindrome("aba") == True
assert Solution().validPalindrome("abca") == True
assert Solution().validPalindrome("eeccccbebaeeabebccceea") == False
