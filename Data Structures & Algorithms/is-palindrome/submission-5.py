class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        l = 0
        r = len(s)-1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1

            char_l = s[l].capitalize()
            char_r = s[r].capitalize()

            if char_l != char_r:
                return False
            
            l += 1
            r -= 1
            
        return True