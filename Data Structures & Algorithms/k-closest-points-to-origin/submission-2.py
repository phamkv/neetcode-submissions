class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x,y = point
            distance = x**2 + y**2
            if len(heap) < k:
                heapq.heappush_max(heap, (distance, point))
            else:
                heapq.heappushpop_max(heap, (distance, point))
        return [point for _, point in heap]