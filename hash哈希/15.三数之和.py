#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            two_res = self.twoSum(nums, i+1, -nums[i])
            if len(two_res) > 0:
                for item in two_res:
                    item.append(nums[i])
                    result.append(item)

        return result

    def twoSum(self, nums, start, target):
        #nums.sort()

        left, right = start, len(nums)-1
        res = []
        
        while left < right:
            lo, ro = nums[left], nums[right]
            sums = nums[left] + nums[right]
            if sums < target:
                left += 1
            elif sums > target:
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                # 跳过重复情况
                while left < right and nums[left] == lo:
                    left += 1
                while left < right and nums[right] == ro:
                    right -= 1
        return res

# @lc code=end

