class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        op = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in op:
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    # stack.append(num1 // num2)
                    
                    stack.append(int(num1 / num2))
        return int(stack.pop())

# O(n) time complexity, O(n) space complexity