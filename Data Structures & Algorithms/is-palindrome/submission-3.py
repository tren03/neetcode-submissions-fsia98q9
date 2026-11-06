class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = ""
        for i in s:
            if ord(i) >= ord("a") and ord(i) <= ord("z"):
                clean_s += i.lower()
                continue
            if ord(i) >= ord("A") and ord(i) <= ord("Z"):
                clean_s += i.lower()
                continue
            if ord(i) >= ord("0") and ord(i) <= ord("9"):
                clean_s += i.lower()
                continue

        l = 0
        r = len(clean_s) - 1
        while l <= r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1

        return True
        