import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        sortedQueries = sorted([i for i in range(len(queries))], key=lambda i: queries[i])

        result = [-1] * len(queries)
        minHeap = []
        i = 0
        for queryIdx in sortedQueries:
            time = queries[queryIdx]
            while i < len(intervals) and intervals[i][0] <= time:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, (length, intervals[i][1]))
                i += 1
            while minHeap and minHeap[0][1] < time:
                heapq.heappop(minHeap)
            if minHeap:
                result[queryIdx] = minHeap[0][0]
        return result
            
