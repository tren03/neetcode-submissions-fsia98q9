class Solution:
    # have a anagram hashmap, with key as word and val as list of anagrams of that word
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isA(str1:str,str2:str) -> bool:
            count1 = {}
            count2 = {}
            for i in str1:
                if i not in count1:
                    count1[i] = 0
                else:
                    count1[i]+=1
            
            for j in str2:
                if j not in count2:
                    count2[j] = 0
                else:
                    count2[j]+=1
        
            return count1==count2
                
                

        m = {}
        for i in strs:
            keys = list(m.keys())
            print(keys)
            flag = False
            for j in keys:
                if isA(j,i):
                    flag = True
                    m[j].append(i)
                    break
            
            if flag == False:
                m[i]=[i]
            print(m)
        
        return m.values()

            
            
            
            

            

            




        