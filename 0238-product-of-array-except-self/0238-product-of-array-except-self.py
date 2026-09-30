class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_array = [0]*len(nums)
        pre_product = 1
        for i in range(len(nums)):
            new_array[i] = pre_product
            pre_product *= nums[i]

        post_prod = 1
        for j in range(len(nums)-1,-1,-1):
            new_array[j] *= post_prod
            post_prod *= nums[j]

        return new_array
