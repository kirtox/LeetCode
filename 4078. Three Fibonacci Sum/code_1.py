class Solution:
    def threeFibonacciSum(self, n: int) -> bool:

        # def Fibonacci(n):
        #     if n == 0:
        #         return 0
        #     elif n == 1:
        #         return 1
        #     else:
        #         return Fibonacci(n-1) + Fibonacci(n-2)

        if n % 2 != 0:
            return False

        first = 0
        second = 1
        while first + second <= (n/2):
            curr = first + second
            if curr < n/2:
                first, second = second, curr
            elif curr == n/2:
                return True
        return False
            
# O(log n) time complexity, O(1) space complexity
