"""
32. Longest Valid Parentheses
 
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
 
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
 
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
"""
 
class Solution:
    def longestValidParentheses(self, s: str):
 
        if len(s) <= 1:return 0
 
        hash_map = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        stack = list()
        stack.append(-1)
        max_len = 0
 
        for idx, c in enumerate(s):
            if c in hash_map.keys():
                stack.append(idx)
            else:
                stack.pop()
 
                if len(stack) == 0:
                    stack.append(idx)
 
                length = idx - stack[-1]
 
                if length > max_len:
                    max_len = length
 
        return max_len
 
d = Solution().longestValidParentheses(s="(()")
print(d)
 
 
 # -----------------------------------------------------------------------

 """
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
"""

class Solution:
    def longestValidParentheses(self, s: str):

        if len(s) <= 1:return 0

        hash_map = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        stack = list()
        stack.append(-1)
        max_len = 0

        for idx, c in enumerate(s):
            if c in hash_map.keys():
                stack.append(idx)
            else:
                stack.pop()

                if len(stack) == 0:
                    stack.append(idx)

                length = idx - stack[-1]

                if length > max_len:
                    max_len = length

        return max_len

d = Solution().longestValidParentheses(s="(()")
print(d)


