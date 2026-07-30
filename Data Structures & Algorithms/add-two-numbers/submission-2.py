# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        cur = ans
        carry = 0


        while l1 and l2:
            res = l1.val + l2.val + carry
            print(res)
            if res >= 10:
                res = res % 10
                carry = 1
            else:
                carry = 0
            print(res, carry)
            cur.next = ListNode(res)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            res = l1.val + carry
            if res >= 10:
                res = res % 10
                carry = 1
            else:
                carry = 0
            cur.next = ListNode(res)
            cur = cur.next
            l1 = l1.next
            
        while l2:
            res = l2.val + carry
            if res >= 10:
                res = res % 10
                carry = 1
            else:
                carry = 0
            cur.next = ListNode(res)
            cur = cur.next
            l2 = l2.next
        
        if carry:
            cur.next = ListNode(carry)

        return ans.next
