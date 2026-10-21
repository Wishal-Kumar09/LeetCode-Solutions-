class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums  = sorted(nums)
        res = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                res.append(i)
        return res
        