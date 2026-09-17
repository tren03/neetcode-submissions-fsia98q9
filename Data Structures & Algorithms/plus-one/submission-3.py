class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            digit = digits[i]
            digit += carry 
            carry = 0
            if digit >= 10:
                carry = digit // 10
                digit = digit % 10
            digits[i] = digit
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits
        