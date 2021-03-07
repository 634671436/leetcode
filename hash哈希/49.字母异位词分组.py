#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # hash table解决问题
        res = []

        new_str_dict = {}
        for item in strs:
            # 这里用sorted 而不是 sort()，因为sorted会生成新的排列后的结果
            new_str = ''.join(sorted(list(item)))        # "eat" -> "aet"
            if new_str not in new_str_dict:
                l = []
                l.append(item)
                new_str_dict[new_str] = l
            else:
                new_str_dict[new_str].append(item)
        
        for k, v in new_str_dict.items():
            res.append(v)
        
        return res
# @lc code=end

