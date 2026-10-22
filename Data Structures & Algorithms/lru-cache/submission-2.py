class Node:
    def __init__(self,key=0,val=0,left=None,right=None):
        self.val=val
        self.key=key
        self.left=left
        self.right=right

class DLL:
    def __init__(self, size):
        self.size = size
        self.head = Node()
        self.tail = Node()
        self.m = {}
    
    def get(self, key):
        if key in self.m:
            self.move_end(self.m[key])
            return self.m[key].val
        return -1
    
    def put(self, key, val):
        if key in self.m:
            # mark used
            self.m[key].val = val
            self.move_end(self.m[key])
            return
        
        # 2 cases - evict / don't evict
        temp = Node(key=key,val=val)

        # don't evict case
        if len(self.m) < self.size:
            self.move_end(temp)
            self.m[key] = temp
            return


        # evict case
        # we need to remove from map
        self.remove_head() 
        self.move_end(temp)
        self.m[key] = temp
    
    def move_end(self,node):
        if self.head.right == node:
            next_node = node.right

            self.head.right = next_node
            next_node.left = self.head

            # tail attachment
            last_node = self.tail.left
            self.tail.left = node
            node.right = self.tail
            node.left = last_node
            last_node.right = node
            return
        
        if self.tail.left == node:
            return


        # first node to insert
        if self.head.right == None:
            self.head.right = node
            node.left = self.head
            node.right = self.tail
            self.tail.left = node
            return
        
        # middle node
        prev = node.left
        nxt = node.right

        if prev != None:
            prev.right = nxt
        if nxt != None:
            nxt.left = prev

        last_node = self.tail.left
        last_node.right = node
        node.left = last_node
        node.right = self.tail
        self.tail.left = node
    
    def remove_head(self):
        if self.head.right == self.tail.left and self.head.right is not None:
            del self.m[self.head.right.key]
            self.head.right = None
            self.tail.left = None
            return
        
        first_node = self.head.right
        new_first_node = first_node.right

        self.head.right = new_first_node
        new_first_node.left = self.head
        del self.m[first_node.key]
        
    

class LRUCache:
    def __init__(self, capacity: int):
        self.dll = DLL(size=capacity)

    def get(self, key: int) -> int:
        return self.dll.get(key)

    def put(self, key: int, value: int) -> None:
        self.dll.put(key,value)
        
