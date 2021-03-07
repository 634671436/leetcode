#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 重点就是维护[0:slow+1]的元素都是不重复的，所以不等的时候就一定要替换
        # 维护的slow和fast之间都是相同的元素，一旦不相同，则slow进到下一步，fast的值赋给slow，维持[0：slow+1]都是不重复的。
        # 看见相同的，i就不动，j还是继续往前走，直到有一个不同的出现。就让i跳到下一个位置，进行替换
        slow = 0
        for fast in range(1, len(nums)):
            # 如果一旦元素不同，则在[i:j]之间相同的就要进行替换
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow+1

# @lc code=end

