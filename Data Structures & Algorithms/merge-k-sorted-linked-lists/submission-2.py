# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we have k ptrs
        head = ListNode()
        ans = head

        heap = []
        heapq.heapify(heap)
        for index,ptr in enumerate(lists):
            if ptr is not None:
                heapq.heappush(heap, (ptr.val,index,ptr))
        if len(heap) == 0:
            return

        while len(heap):
            # we can use a heap for optimization to find the smallest value
            element = heapq.heappop(heap)
            _,index,min_ptr = element
            if min_ptr.next is not None:
                heapq.heappush(heap,(min_ptr.next.val, index, min_ptr.next))


            lists[index] = lists[index].next
            min_ptr.next = None
            head.next = min_ptr
            head = head.next
        return ans.next