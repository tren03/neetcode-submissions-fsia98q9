class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        close = {"(","[","{"}
        for i in s:
            if i in close:
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                else:
                    if st[-1] == closeToOpen[i]:
                        st.pop()
                    else:
                        return False
            
        print(len(st))
        return not bool(len(st))


        
        