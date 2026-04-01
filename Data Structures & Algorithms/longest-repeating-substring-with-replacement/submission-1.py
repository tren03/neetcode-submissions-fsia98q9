class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep adding to set till valid
        # if we hit invalid case, start popping off from l
        # and keep checking for valididty
        # once valid, start adding to set again
        # keep track of the length of the set
        def get_ele_count(hmap):
            total_chars = 0
            for key, value in hmap.items():
                total_chars += value
            return total_chars
            

        def valid(hmap,l,r,k):
            # count of most occuring ele + other elements < k
            max_occurance = 0
            for key, value in hmap.items():
                max_occurance = max(max_occurance,value)
            
            if (r-l+1) - max_occurance <= k:
                return True
            return False
                
        l = 0
        r = 0
        hmap={}
        answer = 0
        while r < len(s):
            if s[r] in hmap:
                hmap[s[r]] += 1
            else:
                hmap[s[r]] = 1 

            if valid(hmap,l,r,k):
                r+=1
                answer = max(answer,get_ele_count(hmap))
                continue
            else:
                while not valid(hmap,l,r,k):
                    # start popping from l till valid
                    if hmap[s[l]] == 1:
                        del hmap[s[l]]
                    else:
                        hmap[s[l]]-=1
                    l+=1

            answer = max(answer,get_ele_count(hmap))
            r+=1
        return answer

                    




        
        