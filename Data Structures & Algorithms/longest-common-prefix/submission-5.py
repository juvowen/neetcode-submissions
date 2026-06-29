class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = strs[0]
        a =""

        for i in range(len(t)):
            for word in strs:
                if i>=len(word) or word[i] != t[i]:
                    return  a
                
            a+=t[i]
        return(a)



