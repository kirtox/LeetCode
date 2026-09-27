class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']

        for ele in tokens:
            if ele not in op:
                stack.append(ele)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                # print(f"num1 ? num2 => {num1} {ele} {num2}")
                if ele == '+':
                    curr = num1 + num2
                    stack.append(curr)
                elif ele == '-':
                    curr = num1 - num2
                    stack.append(curr)
                elif ele == '*':
                    curr = num1 * num2
                    stack.append(curr)
                elif ele == '/':
                    curr = num1 / num2
                    stack.append(curr)
        return int(stack.pop())