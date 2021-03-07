#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # need记录t中需要的字符数量，在滑动窗口中，如果被需要的字符数量一直能满足，则移动left指针
        # window用于记录当前滑动窗口中，被需要的字符的数量。
            # 如果window中统计的各个字符数量，能满足need中需要的情况，则滑动left指针
        need, window = {}, {}
        for s1 in t:
            if s1 not in need:
                need[s1] = 1
            else:
                need[s1] += 1
        
        # left 和 right 两个起始位置为0的指针
        left, right = 0, 0 
        valid = 0
        start = 0
        min_len = len(s)+1

        # 注意： right指针的范围
        while right < len(s):
            # 当前被加入的字符
            c = s[right]
            # right指针在当前字符的前面一个位置，因此截取的时候，min_len就是right-left的长度
            right += 1

            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1

                # 该字符的数量达到need需要的数量
                if window[c] == need[c]:
                    valid += 1

            # 如果被need的字符一直满足要求，则滑动left指针，求最小子串
            while valid == len(need):
                
                # 统计长度并更新
                if right - left < min_len:
                    min_len = right - left
                    start = left

                # 需要被删除的字符，并查看该字符被need的情况。
                # 如果是被需要的，则看其数量是否是need需要的数量。窗口中的A被需要3次，现在A删出了1次，则valid不被满足
                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        if min_len == len(s)+1:
            return ""
        else:
            return s[start:start+min_len]
# @lc code=end

