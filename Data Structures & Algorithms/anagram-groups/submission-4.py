class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i not in m:
                m[sorted_i] = [i]
                continue
            m[sorted_i].append(i)
        
        ans = []
        for key,val in m.items():
            ans.append(val)
        return ans


            
        