class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closetoOpen = {"]" : "[", "}" : "{", ")" : "("}

        for c in s:
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    stack.pop()
                else:
                    return False
            
            else: 
                stack.append(c)

        return True if not stack else False 


#If the stack is empty, every opening bracket had a
        # matching closing bracket, so the string is valid.
        #
        # If the stack is NOT empty, there are unmatched
        # opening brackets, so the string is invalid.
        