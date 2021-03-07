#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}
        left, right = 0, 0
        max_len = 0

        while right < len(s):
            c = s[right]
            right += 1

            if c not in window:
                window[c] = 1
            else:
                window[c] += 1
            
            while window[c] > 1:
                d = s[left]
                window[d] -= 1
                left += 1
            
            if right-left > max_len:
                max_len = right - left
        
        return max_len


# @lc code=end

