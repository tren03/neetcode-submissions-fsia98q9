class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [0,1] - [a,b] b->a
        # create adj first
        indeg = [0] * (numCourses)

        adj = {}
        for p in prerequisites:
            # b - parent
            # a - child
            a = p[0]
            b = p[1]
            adj[b] = adj.get(b,[])
            adj[b].append(a)
            indeg[a] += 1 
        print(indeg)
        print(adj)

        q = []
        for ind,i in enumerate(indeg):
            if i == 0:
                q.append(ind)
        print(q)
        ans = []

        while q:
            popped = q[0]
            q = q[1:]
            n = adj.get(popped,[])
            ans.append(popped)

            for neigh in n:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)
        
        return len(ans) == numCourses



            
        


        