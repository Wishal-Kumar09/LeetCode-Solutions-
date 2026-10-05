class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        st = []
        for i in range(len(s)):
            if s[i] == "(":
                st.append(count)
                count = 0
            else:
                if s[i-1] == "(":
                    count = st[-1] + 1
                else:
                    count = st[-1] + 2*count
                st.pop()
                   
        return count
        