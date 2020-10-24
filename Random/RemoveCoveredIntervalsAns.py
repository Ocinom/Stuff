class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            x = intervals[i]
            if x[0]>=left and x[1]<=right:
                count+=1
            elif x[0]<=right and x[1]>=right:
                right = x[1]
            elif x[0]>right:
                left = x[0]
                right = x[1]

        return len(intervals)-count
