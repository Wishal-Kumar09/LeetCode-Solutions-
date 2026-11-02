class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_element = float('inf')
        steps = 0
        for i in range(len(nums)):
            if nums[i] < min_element:
                min_element = nums[i]

        for j in range(len(nums)):
            steps +=  nums[j] - min_element

        return steps