class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = {}

        for p in prerequisites:
            from_node = p[1]
            to_node = p[0]
            if from_node not in adj:
                adj[from_node] = [to_node]
            else:
                adj[from_node].append(to_node)
            indeg[to_node] += 1
        
        q = []
        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)
            if n not in adj:
                adj[n] = []

        ans = []
        while q:
            popped = q.pop()
            ans.append(popped)

            for neigh in adj[popped]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)
                

        if len(ans) == numCourses:
            return ans
        return []





        