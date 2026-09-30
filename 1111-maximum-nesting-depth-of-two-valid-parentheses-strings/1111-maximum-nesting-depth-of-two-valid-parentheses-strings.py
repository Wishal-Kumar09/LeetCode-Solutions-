class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """


        depth = 0
        new_array = []
        for i in range(len(seq)):
            if seq[i] == '(':
                if i % 2 == 0:
                    new_array.append(0)
                else:
                    new_array.append(1)
                depth += 1
            
            elif seq[i] == ')':
                depth -= 1
                if depth % 2 == 0:
                    new_array.append(0)
                else:
                    new_array.append(1)

        return new_array
