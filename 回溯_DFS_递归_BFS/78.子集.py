#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = [[]]
        trace = []
        self.dfs(nums, trace)
        return self.res

    def dfs(self, nums, trace):

        for i in range(len(nums)):
            trace.append(nums[i])
            self.res.append(list(trace))
            self.dfs(nums[i+1:], trace)
            trace.pop()

# @lc code=end

