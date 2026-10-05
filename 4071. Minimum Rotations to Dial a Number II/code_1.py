class Solution:
    def minRotations(self, n: int, s: str) -> int:
        def dist(a: int, b: int):
            big = max(int(a), int(b))
            small = min(int(a), int(b))
            diff = big - small
            return min(diff, 10-diff)

        edge = [0] * n
        prefix = [0] * n

        for k in range(1, n):
            # print(f"dist({s[k - 1]}, {s[k]})")
            edge[k] = dist(s[k - 1], s[k])
        # print(f"edge: {edge}")
        
        for i in range(1, n):
            # print(f"{prefix[i - 1]} + {edge[i]}")
            prefix[i] = prefix[i - 1] + edge[i]
        # print(f"prefix: {prefix}")
        res = -1
        for i in range(n):
            if i == 0:
                cost = dist("0", s[n - 1])
                cost += prefix[n - 1]
            else:
                """
                cost =
                    dist(0, first char)
                    + internal cost of left part
                    + bridge cost from s[i-1] to s[n-1]
                    + internal cost of right part
                """
                cost = 0
    
                cost += dist("0", s[0])
                cost += prefix[i - 1]
                cost += dist(s[i - 1], s[n - 1])
                cost += prefix[n - 1] - prefix[i]
        
            if res == -1:
                res = cost
            else:
                res = min(res, cost)
        return res

# O(n) time complexity, O(n) space complexity