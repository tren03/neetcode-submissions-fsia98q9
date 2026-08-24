class Node:
    def __init__(self, value=None):
        self.value = value
        self.m = {}
        self.is_end = False


class PrefixTree:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        cur = self.head
        ind = 0
        exists = True

        for ind in range(len(word)):
            v = word[ind]
            links = cur.m
             
            if v not in links:
                exists = False
                break
            else:
                cur = links[v]
        
        if exists:
            cur.is_end = True
            return

            
        
        # ind - the chars we need to insert into prefix

        # all values are already there


        for i in range(ind,len(word)):
            temp = Node(word[i])
            cur.m[word[i]] = temp
            cur = temp

        cur.is_end = True



    def search(self, word: str) -> bool:
        cur = self.head
        ind = 0

        for ind in range(len(word)):
            v = word[ind]
            links = cur.m
             
            if v not in links:
                return False
            else:
                cur = links[v]
        return cur.is_end




    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        ind = 0
        word = prefix

        for ind in range(len(word)):
            v = word[ind]
            links = cur.m
             
            if v not in links:
                return False
            else:
                cur = links[v]
        
        return True
        