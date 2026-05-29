class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h  = {}
        count = 0

        for item in nums:
            if item not in h:
                left = h.get(item-1,0)
                right = h.get(item+1,0)
                currentLen = left+right +1
                count = max(count,currentLen)

                h[item] = currentLen

                h[item - left] = currentLen
                h[item + right] = currentLen

        return count