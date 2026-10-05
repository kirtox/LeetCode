class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [x for x in s.lower() if x.isalnum()]
        
        if len(new_s) == 0:
            return True

        head = 0
        tail = len(new_s) - 1

        while head < tail:
            if new_s[head] != new_s[tail]:
                return False
            head += 1
            tail -= 1    
    
        return True

# O(n) time complexity, O(n) space complexity