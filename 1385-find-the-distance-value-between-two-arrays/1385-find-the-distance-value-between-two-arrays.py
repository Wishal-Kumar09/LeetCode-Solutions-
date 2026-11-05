class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        arr2.sort()
        for i in arr1:
            p = bisect.bisect_left(arr2, i)
            if p == len(arr2) or abs(i - arr2[p]) > d:
                if p == 0 or abs(i - arr2[p - 1]) > d:
                    count += 1
        return count
            