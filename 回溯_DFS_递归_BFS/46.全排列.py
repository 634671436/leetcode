#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        track = []

        self.helper(nums, track)
        return self.res

    def helper(self, nums, track):
        
        if len(track) == len(nums):
            self.res.append(list(track))
        
        for i in nums:
            if i in track:
                continue
            track.append(i)
            self.helper(nums, track)
            track.pop()
# @lc code=end

