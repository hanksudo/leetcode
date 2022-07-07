from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [None] * len(A)
        l = 0
        r = len(A) - 1
        for i in range(len(A))[::-1]:
            if abs(A[l]) > abs(A[r]):
                ans[i] = A[l] * A[l]
                l += 1
            else:
                ans[i] = A[r] * A[r]
                r -= 1
        return ans

if __name__ == "__main__":
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
