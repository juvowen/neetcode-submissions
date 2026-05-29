class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h ={}
        pairs = []
        result = []
        for item in nums:
            h[item] = h.get(item,0)+1

        for item in h:
            count = h[item]
            print(count)
            pairs.append([count, item])

        pairs.sort(reverse = True)

        for i in range(k):
            result.append(pairs[i][1])

        return result