# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = ListNode()
        ans.next = head
        cur = ans

        while cur != None:
            group_prev = cur
            for i in range(k):
                cur = cur.next
                if cur == None:
                    return ans.next
            group_next = cur.next
            kth_element = cur

            # we can logically think of 3 steps
            # ex - 
            # X - 1 - 2 - 3 - Y
            # x = group_prev
            # y = group_next
            # kth = 3
            # wire front -> group.first_element = group_next
            # wire back -> group_prev.next = kth element
            # reverse

            # lets start with wiring 1st group element to group_next
            prev = group_next
            cur_group = group_prev.next

            while cur_group != group_next:
                tmp = cur_group.next
                cur_group.next = prev
                prev = cur_group
                cur_group = tmp
            
            # wire the other element
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp
            cur = group_prev
            
        
        return ans.next
            
            


        

            
                    
















        