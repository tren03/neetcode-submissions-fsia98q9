class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        clean = []
        for i in triplets:
            invalid = False
            for j in range(3):
                if i[j] > target[j]:
                    invalid = True
            if not invalid:
                clean.append(i)
        
        for i in clean:
            for j in range(3):
                if i[j] == target[j]:
                    good.add(j)
        
        return len(good) == 3
                    
                



            


        