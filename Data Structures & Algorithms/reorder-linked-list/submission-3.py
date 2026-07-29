# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half + reverse second half + merge
        s = head 
        f = head
        head1 = head
        prev = None

        while f != None:
            prev = s
            s = s.next
            if f.next == None:
                break
            f = f.next.next
        
        print(prev.val)
        prev.next = None
        # reverse second half 
        cur = s
        prev = None
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head2 = prev
        
        # merge both halfs
        # head, prev - 
        p1 = head
        p2 = prev
        while p1 and p2:
            t1 = p1.next
            t2 = p2.next

            p1.next = p2
            p2.next = t1

            p1 = t1
            p2 = t2
    
        


            

            
            
            



        


        


        
        