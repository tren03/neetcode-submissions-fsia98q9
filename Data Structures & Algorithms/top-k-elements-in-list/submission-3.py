class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        m = {}
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        l = list(m.items())
        l = sorted(l, key=lambda x:x[1])
        n = len(l)
        ans = []
        for i in range(n-1,n-1-k,-1):
            ans.append(l[i][0])
        return ans



        

        