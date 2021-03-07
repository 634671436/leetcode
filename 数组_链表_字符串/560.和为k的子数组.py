#
# @lc app=leetcode.cn id=560 lang=python
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Time Limited
        '''
        res = 0
        for i in range(len(nums)):
            num_sum = nums[i]
            if num_sum == k:
                res += 1

            for j in range(i+1, len(nums)):
                num_sum += nums[j]
                #if num_sum > k:
                #    break
                if num_sum == k:
                    res += 1
        '''
        # 采用前缀和的方式记录nums[:i]的和
        # 方案二：Time Limited
        '''
        n = len(nums)
        pre_sum = [0 for _ in range(n+1)]
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]    
        
        for i in range(len(pre_sum)):
            for j in range(i+1, len(pre_sum)):
                if pre_sum[j] - pre_sum[i] == k:    # -> pre_sum[i] = pre_sum[j] - k, 利用hash table记录
                    res += 1
        '''
        # 方案三：
        prefixSumArray = {0: 1}
        res = 0
        pre_sum = 0

        for num in nums:
            pre_sum += num
            diff = pre_sum - k         # 方案二中的 pre_sum[i] = pre_sum[j] - k， diff即为pre_sum[i]
            # 如果pre_sum[i]存在，即如果有前缀和满足条件，则更新
            if diff in prefixSumArray:
                res += prefixSumArray[diff]
            
            if pre_sum not in prefixSumArray:
                prefixSumArray[pre_sum] = 1
            else:
                prefixSumArray[pre_sum] += 1

        return res
# @lc code=end

