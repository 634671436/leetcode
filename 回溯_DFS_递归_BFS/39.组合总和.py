#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        trace = []
        # 添加排序
        candidates.sort()
        self.dfs(candidates, trace, target)
        return self.res

    def dfs(self, candidates, trace, target):
        
        # 结束条件
        if sum(trace) > target:
            return

        if sum(trace) == target:
            self.res.append(list(trace))

        for i in range(len(candidates)):
            if candidates[i] > target:
                return
            trace.append(candidates[i])
            # 避免重复，从当前元素的之后开始选择
            self.dfs(candidates[i:], trace, target)
            trace.pop()
# @lc code=end

