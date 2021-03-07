#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
            for i in range(1,n) 即对其中的每个节点都作为root节点，来统计左右子树的两种情况
            按照递归的公式来的
            其中，一维数组record来保存n在不同的值时，不同的BST（二叉查找树）的数量
        '''

        '''
        record = [0 for i in range(n+1)]
        record[0] = 1

        i = 1
        while i<=n:
            j=0
            while j < i:
                record[i] += record[j] * record[i-1-j]
                j += 1 
            i += 1
        return record[n]
        '''

        # 备忘录
        mem = dict()
        self._numTrees(1, n, mem)
        return mem[(1, n)]

    # 左右子树的情况相乘（排列组合），而不是相加
    # 时间太长，递归层数太深，导致超时, 因此加入备忘录
    # 递归的处理思想和循环的思想相同，都是从过去的状态推导到新的状态
    def _numTrees(self, left, right, mem):
        if right < left:
            return 1
        if (right-left) == 0:
            mem[(left, right)] = 1
            return 1
        if (right-left) == 1:
            mem[(left, right)] = 2
            return 2

        if (left, right) in mem:
            return mem[(left, right)]

        a = 0
        for i in range(left, right+1):
            m = self._numTrees(left, i-1, mem)
            n = self._numTrees(i+1, right, mem)
            a += m * n
        
        mem[(left, right)] = a
        return a

# @lc code=end

