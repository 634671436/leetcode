#
# @lc app=leetcode.cn id=567 lang=python
#
# [567] 字符串的排列
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        need, window = {}, {}
        for s in s1:
            if s not in need:
                need[s] = 1
            else:
                need[s] += 1
        
        left, right = 0, 0
        valid = 0

        while right < len(s2):
            c = s2[right]
            right += 1

            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(s1):
                if valid == len(need):
                    return True

                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -=1

        return False 
# @lc code=end

