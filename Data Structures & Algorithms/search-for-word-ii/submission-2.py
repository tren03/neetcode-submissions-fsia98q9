class TrieNode:
    def __init__(self):
        self.neigh = {} # {val:TrieNode}
        self.end_value = None # will contain value if node is last letter of word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        head = TrieNode()
        self.ans = set()

        for word in words:
            cur = head
            for letter in word:
                if letter in cur.neigh:
                    cur = cur.neigh[letter]
                else:
                    new_node = TrieNode()
                    cur.neigh[letter] = new_node
                    cur = new_node
            cur.end_value = word
        
        m = len(board)
        n = len(board[0])
    
        def dfs(graph_node, cur_trie, vis):
            i = graph_node[0]
            j = graph_node[1]
            if cur_trie.end_value is not None:
                self.ans.add(cur_trie.end_value)
            if i+1 < m and not vis[i+1][j]:
                a = board[i+1][j]
                if a in cur_trie.neigh:
                    vis[i+1][j] = True
                    dfs((i+1, j), cur_trie.neigh[a], vis)
                    vis[i+1][j] = False
            if i-1 >= 0 and not vis[i-1][j]:
                a = board[i-1][j]
                if a in cur_trie.neigh:
                    vis[i-1][j] = True
                    dfs((i-1, j), cur_trie.neigh[a], vis)
                    vis[i-1][j] = False
            if j+1 < n and not vis[i][j+1]:
                a = board[i][j+1]
                if a in cur_trie.neigh:
                    vis[i][j+1] = True
                    dfs((i, j+1), cur_trie.neigh[a], vis)
                    vis[i][j+1] = False
            if j-1 >= 0 and not vis[i][j-1]:
                a = board[i][j-1]
                if a in cur_trie.neigh:
                    vis[i][j-1] = True
                    dfs((i, j-1), cur_trie.neigh[a], vis)
                    vis[i][j-1] =  False


        for i in range(m):
            for j in range(n):
                cur = board[i][j]
                cur_trie = head
                vis = [[False] * n for _ in range(m)]
                if cur in cur_trie.neigh:
                    vis[i][j] = True
                    dfs((i,j), cur_trie.neigh[cur], vis)
        

        
        return list(self.ans)

        

        