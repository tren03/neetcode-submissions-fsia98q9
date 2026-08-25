# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        
        node_to_remove = l-n

        if node_to_remove == 0:
            return head.next

        prev = None
        cur = head
        while node_to_remove:
            print(cur.val)
            node_to_remove -= 1
            prev = cur
            cur = cur.next

        # remove cur
        prev.next = cur.next
        return head
        

        