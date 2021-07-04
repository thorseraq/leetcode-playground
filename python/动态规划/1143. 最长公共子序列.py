"""
dp[i][j] = dp[i-1][j-1] + 1, text1[i] == text2[j]
dp[i][j] = max(dp[i-1][j], dp[i][j-1]), text1[i] != text2[j]

i = 0, 或者 j = 0时，dp[i][j] = 0
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        # i = [1, m], j = [1, n]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[m][n]