# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans_head = ListNode(0)
        cur = ans_head

        while list1 and list2:
            v1 = list1.val
            v2 = list2.val
            if v1 < v2:
                cur.next = ListNode(v1)
                list1 = list1.next
            else:
                cur.next = ListNode(v2)
                list2 = list2.next
            cur = cur.next
        
        while list1:
            cur.next = ListNode(list1.val)
            list1 = list1.next
            cur = cur.next
        while list2:
            cur.next = ListNode(list2.val)
            list2 = list2.next
            cur = cur.next

        return ans_head.next

            

        