class DLLNode:
    def __init__(self, key, val, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.val = val

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def remove(self, node):
        if node == self.head and node == self.tail:
            # only 1 element
            self.head = None
            self.tail = None
            return

        if node == self.head:
            # move head
            n = node.right
            n.left = None
            self.head = n
            return

        if node == self.tail:
            # move tail
            l = node.left
            l.right = None
            self.tail = l
            return
        
        # node is in middle
        left = node.left
        right = node.right
        left.right = right
        right.left = left
        

    def add(self, node):
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
            return
        
        last = self.tail
        last.right = node
        node.left = last
        node.right = None
        self.tail = node

        
class LRUCache:

    def __init__(self, capacity: int):
        self.m = None # {key->node}
        self.cap = capacity
        self.dll = DLL()
        

    def get(self, key: int) -> int:
        if self.m is None:
            return -1
        
        # self.m is init
        node = self.m.get(key, None)
        if node is None:
            return -1
        
        # node exists
        # reorder the node, so it moves back
        self.dll.remove(node)
        self.dll.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.m is None:
            self.m = {}
            print("adding 10 here")
            node = DLLNode(key,value)
            self.dll.add(node)
            self.m[key] = node
            print(self.dll.head.val)
            return
        
        # map init
        node = self.m.get(key, None)

        if node is None and len(self.m) < self.cap:
            node = DLLNode(key,value)
            self.dll.add(node)
            self.m[key] = node
            return

        if node is None and len(self.m) >= self.cap:
            node = DLLNode(key,value)
            head = self.dll.head
            self.dll.remove(head)
            self.dll.add(node)
            del self.m[head.key]
            self.m[key] = node
            
            return

        # node is not None, just reorder and update val
        node.val = value
        self.dll.remove(node)
        self.dll.add(node)


        return
    

            
            

            
            

        


        
        


        
