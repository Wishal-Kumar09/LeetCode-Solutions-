class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        open = close = res = 0
        for i in range(len(s)):
            if s[i] == '(':
                open += 1
            else:
                close += 1
            if open == close:
                res  = max(res,open + close)
            elif close > open: 
                close = open = 0

        open = close = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ')':
                close += 1
            else:
                open += 1
            if close == open:
                res = max(res,open + close)
            elif open > close:
                open = close = 0

        return res
