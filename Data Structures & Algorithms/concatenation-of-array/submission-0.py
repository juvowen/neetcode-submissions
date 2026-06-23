class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        h = []
        for i in nums:
            h.append(i)

        return nums + h
        