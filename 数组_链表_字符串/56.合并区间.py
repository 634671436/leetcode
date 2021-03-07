#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 按照各个区间的首元素排序，这样区间的交际只能发生在相邻的区间
        intervals.sort(key = lambda x: x[0])
        mergeList = []
        for interval in intervals:
            if len(mergeList) == 0 or mergeList[-1][-1] < interval[0]:
                mergeList.append(interval)
            else:
                mergeList[-1][-1] = max(mergeList[-1][-1], interval[-1])
        return mergeList

# @lc code=end

