class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def add_strings(n1, n2):
            carry = 0
            n1_ptr = len(n1) - 1
            n2_ptr = len(n2) - 1
            ans = []

            while n1_ptr >= 0 and n2_ptr >= 0:
                cur_sum = int(n1[n1_ptr]) + int(n2[n2_ptr]) + carry
                val = cur_sum % 10
                carry = cur_sum // 10
                ans.append(str(val))
                n1_ptr -= 1
                n2_ptr -= 1

            while n1_ptr >= 0:
                cur_sum = int(n1[n1_ptr]) + carry
                val = cur_sum % 10
                carry = cur_sum // 10
                ans.append(str(val))
                n1_ptr -= 1

            while n2_ptr >= 0:
                cur_sum = int(n2[n2_ptr]) + carry
                val = cur_sum % 10
                carry = cur_sum // 10
                ans.append(str(val))
                n2_ptr -= 1
            
            if carry:
                ans.append(str(carry))


            ans.reverse()
            ans = "".join(ans)
            return ans

        if len(num1) > len(num2):
            num1,num2 = num2,num1

        ans = "0"
        for n1_ptr in range(len(num1)-1,-1,-1):
            carry = 0
            cur_ans = []
            leading_zeros = (len(num1)-1) - n1_ptr
            for temp in range(leading_zeros):
                cur_ans.append("0")
            for n2_ptr in range(len(num2)-1,-1,-1):
                if num1[n1_ptr] == "0":
                    break
                p = int(num1[n1_ptr]) * int(num2[n2_ptr]) + carry
                carry = p // 10
                val = p % 10
                cur_ans.append(str(val))
            if carry:
                cur_ans.append(str(carry))
            cur_ans.reverse()
            (cur_ans)
            ans = add_strings(ans, cur_ans)
        return ans
            



        