#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
            动态规划的状态转移方程，假设f(i,j)表示[i,...j]为回文串
            
                    |   1                           ,  i == j
            f(i, j) |   s[i] = s[j]                 ,  j = i+1
                    |   s[i] == s[j] and f(i+1, j-1),  j > i+1

            注意dp数组的遍历顺序
        '''
        
        if s is None:
            return

        lst = list(s)
        len_lst = len(lst)
        p = [[0 for row in range(len_lst)] for col in range(len_lst)]  # 注意二维数组的初始化，直接 * 会有问题
        max_len = 0
        start = 0

        # 从下往上，从左往右遍历
        for i in range(len(lst)-1, -1, -1):
            for j in range(i, len(lst)):
                if i==j:
                    p[i][j] = 1
                elif i+1==j  and lst[i] == lst[j]:
                    p[i][j] = 1
                elif i+1==j  and lst[i] != lst[j]:
                    p[i][j] = 0
                else:
                    if lst[i] == lst[j] and p[i+1][j-1] == 1:
                        p[i][j] = 1
                    else:
                        p[i][j] = 0

                if  p[i][j] == 1 and j-i+1 > max_len:
                    max_len = j-i+1
                    start = i
        

        # 斜着往下遍历
        '''
        for l in range(1, len_lst+1):
            for i in range(0, len_lst-l+1):
                j = l + i - 1
                
                if i==j:
                    p[i][j] = 1
                elif i+1==j  and lst[i] == lst[j]:
                    p[i][j] = 1
                elif i+1==j  and lst[i] != lst[j]:
                    p[i][j] = 0
                else:
                    if lst[i] == lst[j] and p[i+1][j-1] == 1:
                        p[i][j] = 1
                    else:
                        p[i][j] = 0

                if  p[i][j] == 1 and j-i+1 > max_len:
                    max_len = j-i+1
                    start = i
        '''

        return ''.join(lst[start:start+max_len])

# @lc code=end

