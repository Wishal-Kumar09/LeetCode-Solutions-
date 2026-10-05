class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = int(s)
        while s > 0:
            digit = s % 10
            if digit % 2 == 0:
                return str(s)
            else:
                s //= 10
        return ''



        