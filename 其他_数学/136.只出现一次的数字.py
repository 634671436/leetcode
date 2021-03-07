#
# @lc app=leetcode.cn id=136 lang=python
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 两倍set的和 - sum(nums)
        # [4,2,1,2,1]
        # [4,2,1] * 2 - [4,2,1,2,1]
        a = set(nums)
        return sum(a) * 2 - sum(nums)
# @lc code=end

