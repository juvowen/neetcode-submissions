class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for item in nums:
            d[item] = d.get(item,0)+1

        for i in d:
            if d[i] > 1:
                return True
        return  False