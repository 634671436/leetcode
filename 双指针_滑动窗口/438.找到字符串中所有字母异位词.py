#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 方法超时, O(n^2)时间复杂度
        '''
        len_p = len(p)
        new_str_dict = {}
        
        new_p = ''.join(sorted(list(p)))
        new_str_dict[new_p] = [-1]
        
        i = 0
        while i <= len(s) - len_p:
            if s[i] not in p:
                i += 1
                continue
            
            new_str = ''.join(sorted(list(s[i:i+len_p])))
            if new_str in new_str_dict:
                new_str_dict[new_str].append(i)
            
            i += 1
        
        return new_str_dict[new_p][1:]
        '''

        # 异位词问题，无序排列尝试使用滑动窗口解决问题
        need = {}
        for alpha in p:
            if alpha not in need:
                need[alpha] = 1
            else:
                need[alpha] += 1

        window = {}
        valid = 0

        left, right = 0, 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            
            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1
                
                if window[c] == need[c]:
                    valid += 1
            
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)

                d = s[left]
                left += 1

                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        
        return res

# @lc code=end

