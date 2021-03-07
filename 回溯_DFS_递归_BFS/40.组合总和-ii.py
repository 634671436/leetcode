#
# @lc app=leetcode.cn id=40 lang=python
#
# [40] 组合总和 II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        trace = []
        # 添加排序并去重
        candidates.sort()
        self.dfs(0, candidates, trace, target)
        return self.res

    def dfs(self, start, candidates, trace, target):
        
        # 结束条件
        if sum(trace) > target:
            return

        if sum(trace) == target:
            # Time Limited
            #if trace not in self.res:
            self.res.append(list(trace))

        for i in range(start, len(candidates)):
            # 注意：这里i - 1 >= start 限制同一层不能为相同值,例如[1,1,1,2,5,6], target=4
            #                       1
            #  1     [1      1      2      5     6]      这一层start = 1，从索引位置1开始计算，因此是大于start。其他层如start=2同理
            #       可以取  不可以取  
            if candidates[i] == candidates[i-1] and i - 1 >= start:
                continue
            if candidates[i] > target:
                return

            trace.append(candidates[i])
            # 避免重复，从当前元素的之后开始选择
            self.dfs(i + 1, candidates, trace, target)
            trace.pop()
# @lc code=end

