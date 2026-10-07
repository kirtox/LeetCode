class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        # print(sorted_nums)
        triplets = []
        
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = len(sorted_nums) - 1
    
            while left < right:
                # print(f"\n[{i}, {left}, {right}]")
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                # print(f"total {total} = nums[{i}]:({sorted_nums[i]}) + nums[{left}]:({sorted_nums[left]}) + nums[{right}]:({sorted_nums[right]})")

                if total == 0:
                    triplets.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left_val = sorted_nums[left]
                    right_val = sorted_nums[right]
                    while left < right and sorted_nums[left] == left_val: 
                        left += 1
                    while left < right and sorted_nums[right] == right_val: 
                        right -= 1
                     
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        # print(f"triplets: {triplets}")
        return triplets

# O(n^2) time complexity, O(n) space complexity