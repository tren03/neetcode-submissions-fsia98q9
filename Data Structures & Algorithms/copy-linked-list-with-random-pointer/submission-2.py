"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {}
        cur = head
        ans_head = None
        while cur:
            if cur in m:
                cur_clone = m[cur]
            else:
                cur_clone = Node(cur.val)
                m[cur] = cur_clone
                if not ans_head:
                    ans_head = cur_clone
            
            # random
            if cur.random: 
                if cur.random in m:
                    cur_clone.random = m[cur.random]
                else:
                    cur_clone.random = Node(cur.random.val)
                    m[cur.random] = cur_clone.random
            # next 
            if cur.next:
                if cur.next in m:
                    cur_clone.next = m[cur.next]
                else:
                    cur_clone.next = Node(cur.next.val)
                    m[cur.next] = cur_clone.next
            cur = cur.next

        return ans_head

            

                
        