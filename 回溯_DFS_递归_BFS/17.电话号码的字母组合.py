#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        self.match = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],
                      '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}

        self.res = []
        trace = []
        self.dfs(digits, trace, 0)
        return self.res

    # 利用index增加读取word的指定字符，字符型问题用index容易处理，因为不需要修改digits
    # 在39题中，利用 i 避免重复，而这里没有重复，注意！同一层的i与下一层没关系
    def dfs(self, digits, trace, index):
        
        if len(digits) == index:
            self.res.append(''.join(list(trace)))
            return
        
        for alpha in self.match[digits[index]]:
            trace.append(alpha)
            self.dfs(digits, trace, index+1)
            trace.pop()

# @lc code=end

