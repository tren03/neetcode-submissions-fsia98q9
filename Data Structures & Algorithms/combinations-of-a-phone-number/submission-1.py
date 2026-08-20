class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nos = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        ans = []
        def rec(i,t):
            if len(t) == len(digits):
                ans.append(t)
                return

            d = int(digits[i])
            letters = nos[d]
            for letter in letters:
                rec(i+1,t+letter)

        rec(0,"")
        if ans[0] == "":
            return []
            

        return ans
            