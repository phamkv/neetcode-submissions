class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j = stack.pop()[0]
                res[j] = i - j
            stack.append((i, temp))
        return res