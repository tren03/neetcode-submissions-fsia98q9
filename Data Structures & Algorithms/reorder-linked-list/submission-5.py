# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        prev = None
        slow = head
        fast = head

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast is None:
                break
            fast = fast.next

        cur = prev.next
        p = None
        # reverse prev -> None
        while cur:
            t = cur.next
            cur.next = p
            p = cur
            cur = t
        prev = p
        
        
        # merge both nodes, prev = start
        cur = head
        while prev:
            temp = cur.next
            print(temp.val)
            cur.next = prev
            prev = prev.next
            cur = cur.next
            cur.next = temp
            cur = cur.next

        cur.next = None




        