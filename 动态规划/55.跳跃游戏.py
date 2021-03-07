#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 动态规划的思想，记录每个点能跳到的最远距离
        fast_len = 0
        for i in range(0, len(nums)-1):
            fast_len = max(fast_len, i + nums[i])
            # 如果当前点能跳到的最远距离不过当前的坐标位置，即卡住了
            if fast_len <= i:
                return False
    
        return fast_len >= len(nums)-1
# @lc code=end

