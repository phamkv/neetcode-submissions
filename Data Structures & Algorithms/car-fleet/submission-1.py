class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carTuple = [(position[i], speed[i]) for i in range(len(speed))]
        carTuple.sort()
        stack = []
        for i in range(len(carTuple) - 1, -1, -1):
            time = (target - carTuple[i][0]) / carTuple[i][1]
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)