class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        stars = []

        for ind,i in enumerate(s):
            if i == "*":
                stars.append((i,ind))
                continue
            if i == "(":
                st.append((i,ind))
                continue
            if i == ")":
                if not st and not stars:
                    return False
                if st:
                    st.pop()
                else:
                    stars.pop()

        while len(st) and len(stars):
            v = st.pop()
            s = stars.pop()
            if v[1] > s[1]:
                return False
                
        return len(st) == 0


        