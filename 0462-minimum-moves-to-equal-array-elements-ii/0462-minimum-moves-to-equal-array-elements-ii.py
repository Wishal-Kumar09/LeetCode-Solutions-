class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        step = 0
        if len(nums) % 2 != 0:
            median = nums[len(nums)//2]
        else:
            median = (nums[len(nums)//2] + nums[(len(nums)//2) - 1]) / 2
        
        for i in range(len(nums)):
            if nums[i] > median :
                step += nums[i] - median 
            else:
                step += median - nums[i]
        return step
        