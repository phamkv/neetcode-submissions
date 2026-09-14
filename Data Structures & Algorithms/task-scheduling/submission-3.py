class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxH = [] # remainingCount

        count = [0 for _ in range(26)]
        for task in tasks:
            i = ord(task) - ord("A")
            count[i] += 1
        for c in count:
            if c > 0:
                heapq.heappush_max(maxH, c)
        
        time = 1
        cdQ = deque([]) # (nextTime, remainingCount)
        while maxH or cdQ:
            if maxH:
                taskCount = heapq.heappop_max(maxH)
                if taskCount > 1:
                    cdQ.append((time + n + 1, taskCount - 1))
            if maxH or cdQ:
                time = time + 1 if maxH else cdQ[0][0]

            if cdQ and cdQ[0][0] == time:
                    _, remainingCount = cdQ.popleft()
                    heapq.heappush_max(maxH, remainingCount)
        return time
        