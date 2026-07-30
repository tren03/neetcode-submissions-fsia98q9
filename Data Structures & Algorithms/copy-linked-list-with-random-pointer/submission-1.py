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
        ans = Node(0)
        cur = ans
        t = head
        m = {}


        # 1st pass - collect nodes in hash
        while t != None:
            # create copy
            c = Node(t.val,t.next)
            cur.next = c
            cur = cur.next
            m[t] = c
            t = t.next
        
        # ans.next holds the copy

        # 2nd pass - attacing copy
        t = head

        while t != None:
            c = m[t]
            if t.random == None:
                c_random = None
            else:
                c_random = m[t.random]
                c.random = c_random
            t = t.next
        
        return ans.next
        
        

            
        