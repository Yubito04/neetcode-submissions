class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionnaire_s = {}
        dictionnaire_t = {}
        if len(s) != len(t):
            return False
           
        for lettre in s :
            if lettre in  dictionnaire_s:
                dictionnaire_s[lettre] += 1
            else :
                dictionnaire_s[lettre] = 1
            
        for car in t:
            if car in dictionnaire_t:
                dictionnaire_t[car] += 1
            else :
                dictionnaire_t[car] = 1    

        return dictionnaire_s == dictionnaire_t    

            
        
        
        
    
        

     
        