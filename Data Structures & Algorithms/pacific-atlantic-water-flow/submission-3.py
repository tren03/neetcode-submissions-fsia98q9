class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pset = [] 
        qset = [] 

        p = set()
        q = set()

        n = len(heights)
        m = len(heights[0])
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    pset.append((i,j))
                    p.add((i,j))
                if i == n-1 or j == m-1:
                    qset.append((i,j))
                    q.add((i,j))
            
        while pset:
            popped = pset[0]
            i = popped[0]
            j = popped[1]
            pset = pset[1:]
            cur_height = heights[i][j]
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for c in d:
                new_i = i + c[0]
                new_j = j + c[1]
                if new_i >= n or new_j >= m or new_i < 0 or new_j < 0:
                    continue
                new_height = heights[new_i][new_j] 
                if (new_i,new_j) not in p and new_height >= cur_height:
                    p.add((new_i,new_j))
                    pset.append((new_i,new_j))

        while qset:
            popped = qset[0]
            i = popped[0]
            j = popped[1] 
            qset = qset[1:]
            cur_height = heights[i][j]
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for c in d:
                new_i = i + c[0]
                new_j = j + c[1]
                if new_i >= n or new_j >= m or new_i < 0 or new_j < 0:
                    continue
                new_height = heights[new_i][new_j] 
                if (new_i,new_j) not in q and new_height >= cur_height:
                    q.add((new_i,new_j))
                    qset.append((new_i,new_j))

        a = list(p.intersection(q))
        a.sort()
        return a


                    
        