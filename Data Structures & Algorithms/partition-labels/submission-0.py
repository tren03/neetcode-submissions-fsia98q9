class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for ind,i in enumerate(s):
            last[i] = ind
        print(last)
        
        res = []
        l = 0 
        r = 0
        last_index = 0
        while r < len(s):
            last_index = max(last_index,last[s[r]])
            print(last_index)
            if r == last_index:
                print("here")
                res.append(last_index-l+1)
                l = r = last_index + 1
                continue
            r += 1
            

        return res
        
