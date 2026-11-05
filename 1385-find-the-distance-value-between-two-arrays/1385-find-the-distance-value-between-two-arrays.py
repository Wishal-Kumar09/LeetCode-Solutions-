class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(arr1):
            flag = False
            j = 0
            while j < len(arr2):
                if abs(arr1[i]-arr2[j]) > d:
                    flag = True
                else:
                    flag = False
                    break
                    i += 1
                j += 1
            if flag == True:
                count += 1
            i += 1

        return count
            