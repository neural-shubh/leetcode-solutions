class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            
            else:
                stack.pop()

            if not stack:
                stack.append(i)
            
            length = i - stack[-1]
            max_length = max(max_length, length)
            pass

        return max_length