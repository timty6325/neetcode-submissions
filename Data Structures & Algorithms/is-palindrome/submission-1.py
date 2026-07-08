class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = "".join(c for c in s if c.isalpha() or c.isdigit())
        pal = pal.lower()

        if len(pal) == 0:
            return True
        if len(pal) == 1:
            return True
        
        else:
            if pal[0] != pal[-1]:
                return False 
            return self.isPalindrome(pal[1:-1])