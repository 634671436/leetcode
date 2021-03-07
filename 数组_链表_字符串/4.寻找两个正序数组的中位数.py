#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 快排 + 索引
        nums = nums1 + nums2
        new_nums = self.QuickSort(nums)
        if len(new_nums) % 2 == 0:
            return (new_nums[len(new_nums)/2 - 1] + new_nums[len(new_nums)/2])*1.0 / 2
        else:
            return new_nums[len(new_nums)/2]
    
    def QuickSort(self, nums):
        
        # 递归结束条件判断错误
        #left, right = 0, len(nums)-1
        #if left >= right:
        #   return
        if len(nums) == 1:
            return nums

        mid = len(nums) / 2
        left_array = self.QuickSort(nums[:mid])
        right_array = self.QuickSort(nums[mid:])
        return self.MergeTwoArray(left_array, right_array)

    def MergeTwoArray(self, array1, array2):

        array = []
        i, j = 0, 0
        # 注意判断条件
        while i < len(array1) and j < len(array2):
            lo, ro = array1[i], array2[j]
            if lo < ro:
                array.append(lo)
                i += 1
            elif lo > ro:
                array.append(ro)
                j += 1
            else:
                array.append(lo)
                array.append(ro)
                i += 1
                j += 1
        
        if i < len(array1):
            array.extend(array1[i:])

        if j < len(array2):
            array.extend(array2[j:])

        return array

# @lc code=end

