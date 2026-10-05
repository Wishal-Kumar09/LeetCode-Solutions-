class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = 0
        num_b = 0

        for  i in range(len(a)-1,-1,-1):
            if a[i] == '1':
                num_a += 2 **(len(a)-1 - i)

        for j  in range(len(b)-1,-1,-1):
            if b[j] == '1':
                num_b += 2 **(len(b)-1-j)
 
        return format(int(num_a) + int(num_b),'b')