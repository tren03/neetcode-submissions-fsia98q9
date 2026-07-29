# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        cur = head
        prev = None
        total = 0

        while cur != None:
            total += 1
            cur = cur.next
            
        from_first = (total - n) + 1
        print(from_first)
        cur = head

        # removing first and last cases
        print("test",n, from_first)
        if from_first == 1:
            # remove first
            head = head.next
            return head
            
            

            

        while cur != None:
            print(i, from_first)
            if i == from_first:
                # remove cur node
                t = cur.next
                prev.next = t
                cur = t
                break
            prev = cur
            cur = cur.next
            i += 1
        return head
            
            




        