#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] 每日温度
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 单调递增栈
        n = len(T)
        res = [0 for _ in range(n)]
        # 栈内存索引
        stack = []

        # 逆序进栈，正序出栈
        for i in range(n-1, -1, -1):
            # 栈的结构，从上往下看是单调递增，越上面的元素位置，在原始数据中越前
            # 如果当前元素大于栈顶元素，则将栈顶元素弹出，因为此时栈堆元素后序无效，有比它更大的元素存在了
            # 如果比栈顶元素小，则保留。
            while len(stack) > 0 and T[i] >= T[stack[-1]]:
                stack.pop()
            
            if len(stack) == 0:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            
            stack.append(i)
        
        return res
        
# @lc code=end

