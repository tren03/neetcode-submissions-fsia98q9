class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.split(" ")
        t = "".join(t)
        print(t)

        t = ""
        for i in s:
            if i.isalnum():
                t += i.lower()
        print(t)

        l = 0
        r = len(t) - 1

        while l <= r:
            if t[l] != t[r]:
                return False
            l += 1
            r -= 1
        return True
        