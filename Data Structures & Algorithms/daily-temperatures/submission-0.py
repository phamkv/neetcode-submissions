class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    index = stack.pop()
                    result[index] = i - index
                stack.append(i)
        return result