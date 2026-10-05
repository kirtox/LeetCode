class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = {
            'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',
            'z',
            '0', '1', '2', '3', '4',
            '5', '6', '7', '8', '9'
        }

        lower_s = s.lower()
        new_s = [x for x in lower_s if x in alphanumeric]
        
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