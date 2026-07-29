# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        head = None

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                small = list1.val
                s = 1
            else:
                small = list2.val
                s = 2
            if ans == None:
                ans = ListNode(val=small)
                head = ans
            else:
                ans.next = ListNode(val=small)
                ans = ans.next
            if s == 1:
                list1 = list1.next
            if s == 2:
                list2 = list2.next

        
        while list1 != None:
            if ans == None:
                ans = ListNode(val=list1.val)
                head = ans
            else:
                ans.next = ListNode(val=list1.val)
                ans = ans.next
            list1 = list1.next

        while list2 != None:
            if ans == None:
                ans = ListNode(val=list2.val)
                head = ans
            else:
                ans.next = ListNode(val=list2.val)
                ans = ans.next
            list2 = list2.next

        return head





        