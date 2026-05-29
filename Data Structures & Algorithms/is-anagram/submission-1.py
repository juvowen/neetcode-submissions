class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        d2 =  {}
        for char in s:
            d[char] = d.get(char,0)+1
        for char in t:
            d2[char] = d2.get(char,0)+1

        if d == d2:
            return True
        return False

        
