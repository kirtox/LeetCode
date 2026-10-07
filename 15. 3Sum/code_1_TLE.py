class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = {}
        
        for i, val in enumerate(nums):
            curr_target = -val

            visited = set()

            for _i, _val in enumerate(nums):
                if i == _i:
                    continue
                
                remaining = curr_target - _val
                if remaining not in visited:
                    visited.add(_val)
                else:
                    triplet = sorted([-curr_target, _val, remaining])
                    key = tuple(triplet)
                    print(f"key: {key}, triplet: {triplet}")
                    if len(triplet) == 3 and triplets.get(key, -1) == -1:
                        triplets[key] = triplet

        return list(triplets.values())

# O(n^2) time complexity, O(n) space complexity
#Output Limit Exceeded 312 / 316 testcases passed