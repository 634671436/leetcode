#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = { ')':'(', '}':'{', ']':'[' }
        # 模拟栈的结构
        stack = []

        for char in s:
            # 左边的括号进栈
            if char in dic.values():
                stack.append(char)
            # 右边的括号 匹配 从栈中弹出的括号结构  ‘)’ -> '('
            elif char in dic.keys():
                if len(stack) == 0 or dic[char] != stack.pop():
                    return False
            else:
                return False
        
        return stack == []
# @lc code=end

