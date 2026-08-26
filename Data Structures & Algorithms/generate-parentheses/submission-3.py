class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        def rec(o,c,arr):
            print(o,c,arr)
            if o == n and c == n:
                ans.append(arr)
                return
            if c > o:
                return
            
            if o < n:
                rec(o+1,c,arr+"(")
                
            if c < n:
                rec(o,c+1,arr+")")
                
        rec(0,0,"")

        return ans

        
        