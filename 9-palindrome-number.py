# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)

        low = 0
        high = len(s) - 1

        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1

        return True

assert Solution().isPalindrome(1000021) == False
assert Solution().isPalindrome(121) == True
assert Solution().isPalindrome(-121) == False
