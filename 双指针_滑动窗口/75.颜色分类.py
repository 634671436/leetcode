#
# @lc app=leetcode.cn id=75 lang=python
#
# [75] 颜色分类
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 设置红、白、蓝三种指针，保证
        # 红色指针左边全为0，
        # 蓝色指针右边全为2，
        # 白色指针指向的全为1

        # white指针从左往右，知道white>blue退出
        # 如果nums[white] == 0，就和red的值互换，red++且white++，因为此时前指针换过来的一定是白色，white已经扫描过那些点了
        # 如果nums[white] == 2, 就和blue互换，blue--，此时white不能++，因为不确定换过来的颜色是什么
        # 如果为1，则自动加1
        n = len(nums)
        red, white, blue = 0, 0, n-1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1  # 注意此时white指针移动
            elif nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            else:
                white += 1
        
        return nums      
# @lc code=end

