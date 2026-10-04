class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = j = curr_sum = max_sum = 0
        set_ = set()
        while i < len(nums) - k + 1:
            if nums[j] in set_:
                set_.remove(nums[i])
                curr_sum -= nums[i]
                i += 1
            else:
                curr_sum += nums[j]
                set_.add(nums[j])
                if (j-i+1) == k:
                    max_sum = max(curr_sum,max_sum)
                    curr_sum -= nums[i]
                    set_.remove(nums[i])
                    i += 1
                j += 1
                
           

        return max_sum