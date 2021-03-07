#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        max_water = 0

        while i<j:
            cur_water = (j-i) * min(height[i], height[j])
            if cur_water > max_water:
                max_water = cur_water
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_water

# @lc code=end

