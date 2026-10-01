class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}

        for i in range(len(s)):
            if mapping.get(s[i], -1) == -1:
                mapping[s[i]] = 1
            else:
                mapping[s[i]] += 1

        # print(f"mapping: {mapping}")
        
        for i in range(len(t)):
            if mapping.get(t[i], -1) == -1:
                return False
            else:
                if mapping[t[i]] == 0:
                    return False
                mapping[t[i]] -= 1
        
        # print(f"mapping: {mapping}")
        return True

# O(n) time complexity, O(n) space complexity