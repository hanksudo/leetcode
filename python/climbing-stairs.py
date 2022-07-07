# https://leetcode.com/problems/climbing-stairs/

# Recursive
# def climbStairs(n: int) -> int:
#     if n in (1, 2):
#         return n
#     return climbStairs(n - 1) + climbStairs(n - 2)

# Dynamic Programming
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    dp = [None] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == "__main__":
    assert climbStairs(5) == 8
    assert climbStairs(50) == climbStairs(49) + climbStairs(48)
