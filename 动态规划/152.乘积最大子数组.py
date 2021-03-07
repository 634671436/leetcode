#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 维护到dp1和dp2，其中dp1[i]表示以nums[i]为结尾的最大乘积，dp2[i]表示以nums[i]为结尾的最小乘积（因为存在负值，乘以负数变成最大的数）
        # 由于每次都不确定正负，因此最大值和最小值是在三者之间比较，如[-2, 3, -4]
        dp1 = [1 for _ in range(len(nums))]
        dp2 = [1 for _ in range(len(nums))]

        dp1[0] = nums[0]
        dp2[0] = nums[0]
        max_num = nums[0]

        for i in range(1, len(nums)):
            dp1[i] = max(dp1[i-1]*nums[i], nums[i], dp2[i-1]*nums[i]) 
            dp2[i] = min(dp1[i-1]*nums[i], nums[i], dp2[i-1]*nums[i])
            max_num = max(max_num, dp1[i])

        return max_num
            
# @lc code=end

