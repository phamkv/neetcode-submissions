class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones.copy()
        heapq.heapify_max(heap)
        while len(heap) > 1:
            first = heapq.heappop_max(heap)
            second = heapq.heappop_max(heap)
            if first > second:
                new_weight = first - second
                heapq.heappush_max(heap, new_weight)
        return 0 if not heap else heap[0]