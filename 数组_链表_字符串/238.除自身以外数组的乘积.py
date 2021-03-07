#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # 遍历两边，一遍是元素左侧的乘积，一遍是元素右侧的乘积，相乘得到最终结果
        left_res = [1 for _ in range(n)]

        for i in range(1, n):
            left_res[i] = left_res[i-1] * nums[i-1]
        
        right_res = [1 for _ in range(n)]
        for j in range(n-2, -1, -1):
            right_res[j] = right_res[j+1] * nums[j+1]
        
        res = []
        for i in range(n):
            res.append(left_res[i] * right_res[i])
        
        return res
        
# @lc code=end

