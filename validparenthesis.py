class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if ( stack[:-1] == '(' and s[i] == ')' ) or ( stack[:-1] == '{' and s[i] == '}' ) or ( stack[:-1] == '[' and s[i] == ']' ):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
