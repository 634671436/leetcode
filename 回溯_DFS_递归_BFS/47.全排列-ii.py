#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        self.res = []
        track = []

        self.helper(nums, track)
        return self.res


    def helper(self, nums, track):

        if len(track) == len(nums):
            self.res.append(list(track))
        
        for i in nums:
            if i>0 and nums[i] == nums[i-1]:
                continue

            track.append(i)
            self.helper(nums, track)
            track.pop()

# @lc code=end

