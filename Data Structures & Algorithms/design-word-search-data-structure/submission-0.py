class Node:
    def __init__(self, val=None,children=None):
        self.val = val
        self.children = children # dict of val:Node
        self.word_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node(val=-1, children={})

    def addWord(self, word: str) -> None:
        # we walk the tree and see if the letter exist
        # if it does move in that branch, else create node 
        r = self.root
        for l in word:
            if l in r.children:
                r = r.children[l]
            else:
                # create 
                new = Node(l,{}) 
                r.children[l] = new
                r = new
        # as last r, mark as end word
        r.word_end = True
        

    def search(self, word: str) -> bool:
        r = self.root

        def rec(i,r):
            if i >= len(word) and r.word_end:
                return True
            if i >= len(word) and not r.word_end:
                return False
            if not r.children:
                return False
            
            cur_node = r
            val_to_search = word[i]

            # i can either be a . or letter
            if val_to_search != ".":
                if val_to_search in r.children:
                    return rec(i+1, r.children[val_to_search])
                else:
                    return False
            
            # i is a dot
            for child in r.children.values():
                temp = rec(i+1, child)
                if temp:
                    return True
            return False
        
        return rec(0, r)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)