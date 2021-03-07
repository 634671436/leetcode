#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        left = 0
        lens = len(needle)

        while left < len(haystack):
            if haystack[left] == needle[0]:
                right = left
                if right + lens < len(haystack) + 1 and haystack[right:right+lens] == needle:
                    return left
            left += 1
        
        return -1

# @lc code=end

