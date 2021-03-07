#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
            
        # 对于位置i而言，val[i]表示可以装的雨水：
        # val[i] = min(
        #               max(height[:i]),    表示i左边最高的位置
        #               max(height[i:])，   表示i右边最高的位置
        #              ) - height[i]
        # 暴力解法
        total_val = 0
        '''
        for i in range(len(height)):
            l_max, r_max = 0, 0
            
            for j in range(0, i+1):
                l_max = max(l_max, height[j])
            
            for j in range(i,len(height)):
                r_max = max(r_max, height[j])
            
            total_val += min(l_max, r_max) - height[i]
        
        return total_val
        '''

        # 带备忘录的解法
        # l_max[i]：表示节点i左边的最大值，初始化l_max[0] = height[0]
        # r_max[i]：表示节点i右边的最大值, 初始化r_max[0] = height[n-1] 
        l_max = [0 for _ in range(len(height))]
        r_max = [0 for _ in range(len(height))]
        l_max[0] = height[0]       
        r_max[len(height)-1] = height[len(height)-1]

        for i in range(1,len(height)):
            l_max[i] = max(l_max[i-1], height[i])

        for i in range(len(height)-2, -1, -1):
            r_max[i] = max(r_max[i+1], height[i])
        
        for i in range(len(height)):
            total_val += min(l_max[i], r_max[i]) - height[i]
        
        return total_val

# @lc code=end

