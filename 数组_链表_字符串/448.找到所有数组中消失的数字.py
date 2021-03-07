#
# @lc app=leetcode.cn id=448 lang=python
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1

        for i in range(1, len(nums)+1):
            if i not in num_dict:
                res.append(i)

        return res 
# @lc code=end

