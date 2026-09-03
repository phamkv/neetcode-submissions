class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carFleetTuple = []
        for i in range(len(position)):
            carFleetTuple.append((position[i], speed[i]))
        sortedCars = sorted(carFleetTuple, key=lambda x: -x[0])
        stack = []
        for carFleet in sortedCars:
            time = (target - carFleet[0]) / carFleet[1]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
                