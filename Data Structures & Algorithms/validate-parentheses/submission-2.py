class Solution:
    def isValid(self, s: str) -> bool:
        a ={
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        #open brackets put in a stack

        for char in s:
            if char in a: 
                #start with open bracket
                stack.append(char)
            else:
                # we see a closing bracket
                if not stack:
                    return False
                popped = stack.pop()

                if a[popped] != char:
                    return False
        return len(stack) == 0



        