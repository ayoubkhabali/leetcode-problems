class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
            if s1 == s2 :
                return True

            if len(s1) != len(s2) :
                return False
            
            if sorted(s1) == sorted(s2) :
                counter = 0
                for i,j in zip(s1,s2) :
                    if i == j : counter += 1 
                if counter+2 == len(s1) :
                    return True
                else :
                    return False
            else : 
                return False
            
        
                