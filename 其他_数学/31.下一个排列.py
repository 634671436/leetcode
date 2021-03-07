#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1 6 8 7 4 3 2
        # <- 从右向左，自倒数第二个数开始，找到第一个比它右边数小的数，称为permutation， 6
        # <- 从右向左，寻找第一个比permutation大的数， 7
        # 交换, 6<->7, 即1 7 8 6 4 3 2
        # 从permutation开始的数，右边的整体逆序，即 1 7 2 3 4 6 8 
        permutaion = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                permutaion = i
                break
        if permutaion == -1:
            nums.reverse()
        else:
            for i in range(len(nums)-1, permutaion, -1):
                if nums[i] > nums[permutaion]:
                    nums[i], nums[permutaion] = nums[permutaion], nums[i]
                    break
        
            nums[permutaion+1:] = nums[permutaion+1:][::-1]
# @lc code=end

