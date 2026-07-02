class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0]) #sort by  their starting point[x,0]


        merged = [intervals[0]]

        for start,end in intervals[1:]:
            lastStart,lastEnd = merged[-1]
            if start<=lastEnd:
                #there is overlap
                merged[-1][1] = max(lastEnd,end)
            else:
                merged.append([start,end])
        return merged




