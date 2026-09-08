class Solution:
    def isHappy(self, n: int) -> bool:
        """
        123 
        123 % 10 = 3
        123 / 10 = 12
        10:22 mins
        """
        seen = set()
        while True:
            s = 0
            while n > 0:
                print(n)
                digit = n % 10
                n = n // 10
                s += digit * digit
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
            n = s




        