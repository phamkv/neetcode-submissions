class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heapq.heapify(result)
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(result, [-dist, [x,y]])
            if len(result) > k:
                heapq.heappop(result)
        return [point for dist,point in result]