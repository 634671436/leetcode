#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 小顶堆的模块
        import heapq

        # 建立小顶堆，当元素个数小于K时继续增加
        pq = []
        for num in nums:
            if len(pq) < k:
                heapq.heappush(pq, num)
            elif num > pq[0]:
                heapq.heapreplace(pq, num)
        
        return heapq.heappop(pq)
# @lc code=end

