class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        types_dict = {}

        for ele in strs:
            curr_dict = {}
            for char in ele:
                if curr_dict.get(char, -1) == -1:
                    curr_dict[char] = 1
                else:
                    curr_dict[char] += 1
            # print(f"curr_dict: {curr_dict}")
            # print(f"tuple curr_dict: {str(sorted(curr_dict))}")
            key = "".join([str(curr_dict[k])+k for k in sorted(curr_dict.keys())])
            # print(f"key: {key}")
            if types_dict.get(key, -1) == -1:
                types_dict[key] = [ele]
            else:
                types_dict[key].append(ele)

        # print(f"types_dict: {types_dict}")

        # return [val for val in types_dict.values()]
        return list(types_dict.values())

# O(n * m) time complexity, O(n * m) space complexity