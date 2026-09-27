class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        op = {'+', '-', '*', '/'}

        for ele in tokens:
            if ele not in op:
                stack.append(int(ele))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
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
                    # Do not use // operator because it truncates towards negative infinity, 
                    # which is not the desired behavior for this problem. 
                    # Instead, use int() to truncate towards zero.
                    # Use int() to truncate towards zero
                    curr = int(num1 / num2) 
                    stack.append(curr)
        return stack.pop()