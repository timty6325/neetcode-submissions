class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
       
        
        for num in tokens:
            if num not in ['+','*','/','-']:
                stack.append(int(num))
            else:
                right = stack.pop()
                left = stack.pop()

                if num == "+":
                    result = right + left
                elif num == "*":
                    result = right * left
                elif num == "-":
                    result = left - right
                else:
                    result = int(left / right)
                stack.append(result)
                
                
        return stack[0]

