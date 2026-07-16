class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)

            else:
                if len(stack) == 0:
                    return False

                curr = stack.pop()

                if curr == '(' and char != ')':
                    return False
                if curr == '[' and char != ']':
                    return False
                if curr == '{' and char != '}':
                    return False
        return len(stack) == 0
                
                


