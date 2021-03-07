#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m, n = len(s), len(s)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # base case
        for i in range(m-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif j == i + 1 and s[i] == s[j]:
                    dp[i][j] = 1
                elif j == i + 1 and s[i] != s[j]:
                    dp[i][j] = 0
                else:
                    assert j > i + 1
                    if s[i] == s[j] and dp[i+1][j-1] == 1:
                        dp[i][j] = 1

        return sum([sum(dp[i]) for i in range(n)])
        
# @lc code=end

