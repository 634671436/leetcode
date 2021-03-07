#
# @lc app=leetcode.cn id=581 lang=python
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        # 无法处理[1,3,2,2,2]的 逆序4
        if len(nums) == 1:
            return 0

        pos = []
        n = len(nums)

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                pos.append([i, i+1])
        
        if len(pos) == 0:
            return 0
        else:
            return pos[-1][-1] - pos[0][0] + 1
        '''
        # 将数组进行排序，比较new_nums和nums
        # 第一个不相同的位置就是最开始的位置，最后一个不相同的位置就是最后的位置
        new_nums = sorted(nums)
        left, right = 0, -1
        for i in range(len(nums)):
            if nums[i] != new_nums[i]:
                left = i
                break
        
        for i in range(len(nums)):
            if nums[i] != new_nums[i]:
                right = i
            
        return right - left + 1
# @lc code=end

