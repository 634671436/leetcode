#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        # dp[i] 表示以s[i]为结尾的词是否可以拆分
        # dp[i] = s[:i] in wordDict or s[j+1:i+1] in wordDict and dp[j] == 1 
        dp = [0 for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if s[:i+1] in wordDict or dp[j] == 1 and s[j+1:i+1] in wordDict:
                    dp[i] = 1
                    break
        
        return dp[-1] == 1
# @lc code=end

