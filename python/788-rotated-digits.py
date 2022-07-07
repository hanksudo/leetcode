# https://leetcode.com/problems/rotated-digits
# https://leetcode.com/problems/rotated-digits/discuss/117975/Java-dp-solution-9ms

# Dyanmic programming
class Solution:
    def rotatedDigits(self, N: int) -> int:
        dp = [0] * (N + 1)
        count = 0
        for i in range(N + 1):
            if i < 10:
                if i in (0, 1, 8):
                    dp[i] = 1
                elif i in (2, 5, 6, 9):
                    dp[i] = 2
                    count += 1
            else:
                x = dp[i // 10]
                y = dp[i % 10]
                if x == y == 1:
                    dp[i] = 1
                elif x >= 1 and y >= 1:
                    dp[i] = 2
                    count += 1
        return count
