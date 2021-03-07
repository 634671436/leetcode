#
# @lc app=leetcode.cn id=263 lang=python
#
# [263] 丑数
#

# @lc code=start
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        
        return num == 1
# @lc code=end

