class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        
        primes = self.allPrimes(n)
        # print(f"primes: {primes}")

        visited = []
        curr_sum = 0
        for prime in primes:
            curr_sum += prime
            if curr_sum <= s:
                visited.append(prime)
        return visited
            
    def allPrimes(self, n: int) -> list[int]:
            # [0, 0, 1, 1, 1, 1, 1, 1]
            #  0  1  2  3  4  5  6, 7
            #->   1  2  3  4  5  6  7
            cand = [1] * (n + 1)
            cand[0] = 0
            cand[1] = 0
            
            # print(f"cand: {cand}")
            
            i = 2
            
            while i <= n:
                if cand[i] == 1:
                    curr_sum = i + i
    
                    while curr_sum <= n:
                        cand[curr_sum] = 0
                        curr_sum += i
                i += 1
                    
            return [k for k, v in enumerate(cand) if v == 1]
    
# O(nloglogn) time complexity, O(n) space complexity# 