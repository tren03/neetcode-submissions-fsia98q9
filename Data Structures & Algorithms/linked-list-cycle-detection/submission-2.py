# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head
        while f != None:
            s = s.next
            if f.next == None:
                return False
            f = f.next.next
            if s == f:
                return True
        return False
        