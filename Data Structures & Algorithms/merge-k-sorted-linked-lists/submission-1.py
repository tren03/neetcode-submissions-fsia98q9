# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we have k ptrs
        head = ListNode()
        ans = head
        temp = []
        while True:
            min_ptr, min_index = None, None

            for index,ptr in enumerate(lists):
                # ptr is the head
                if ptr is None:
                    continue

                # calc min_ptr
                if min_ptr is None:
                    min_ptr = ptr
                    min_index = index
                
                if min_ptr.val > ptr.val:
                    min_ptr = ptr
                    min_index = index
                    continue

            if min_ptr is None:
                break

            lists[min_index] = lists[min_index].next
            min_ptr.next = None
            head.next = min_ptr
            head = head.next
        return ans.next