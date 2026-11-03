class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_element = float('-inf')
        step = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > max_element:
                max_element = nums[i]
        return ((n*max_element) - sum(nums))
        