class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = {}
        for i in range(n+1):
            cooldown[i] = []
        freq = {}
        schedule = []
        heapq.heapify(schedule)
        result = 0
        for task in tasks:
            if task not in freq:
                freq[task] = 0
            freq[task] += 1
        for task, f in freq.items():
            heapq.heappush(schedule, (-f, task))
        cycle = 0
        completed = 0
        while completed < len(tasks):
            while len(cooldown[cycle]) > 0:
                f, task = cooldown[cycle].pop()
                heapq.heappush(schedule, (f, task))
            if schedule:
                f, task = heapq.heappop(schedule)
                if f+1 < 0:
                    cooldown[cycle].append((f+1, task))
                completed += 1
            cycle = cycle + 1 if cycle < n else 0
            result += 1
        return result