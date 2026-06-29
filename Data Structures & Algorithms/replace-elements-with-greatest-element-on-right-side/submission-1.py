class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = -1

        for i in  range(len(arr) -1,-1,-1):
            curr = arr[i]
            arr[i] = n
            n = max(n,curr)
        return arr
        