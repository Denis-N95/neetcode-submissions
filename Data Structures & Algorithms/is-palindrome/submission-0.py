class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [c.lower() for c in s if c.isalnum()]
        return  new == new[::-1]