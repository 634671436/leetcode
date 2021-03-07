#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # hash-table
        num_dict = {}
        
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        
        num_sort = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)
        return [key for key, value in num_sort[:k]]

        # heap
        # 建立小顶堆，求TopK问题：
        #   1.当堆中元素小于K时：则插入元素
        #   2.当堆中元素大于K时，则比较元素出现次数与堆顶元素大小
        #       2.1 如果元素出现次数小于堆顶元素则继续；
        #       2.2 如果元素出现次数大于堆顶元素，则弹出堆顶元素，并插入
# @lc code=end

