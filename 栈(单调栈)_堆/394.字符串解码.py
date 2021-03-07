#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # stack 栈中存储"["前的字符及倍数，如"3[a2[c]]"，对于第一个"["而言，当前存储的为[('', 3)]，而第二次是则存储为[('', 3), ('a', 2)]
        # 因为ans中都是将front_char + ，保证前面的字符一定在前面
        stack = []
        num = 0
        ans = ""

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((ans, num))
                # 添加后，需要重置"["前元素及倍数
                ans, num = "", 0
            elif c == "]":
                front_char, cur_num = stack.pop()
                ans = front_char + cur_num * ans
            else:
                ans += c
        
        return ans

# @lc code=end

