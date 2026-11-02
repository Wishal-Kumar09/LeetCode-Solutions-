class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_element = float('inf')
        n = len(nums)
        for i in range(n):
            if nums[i] < min_element:
                min_element = nums[i]

        return sum(nums) - (n * min_element)

       