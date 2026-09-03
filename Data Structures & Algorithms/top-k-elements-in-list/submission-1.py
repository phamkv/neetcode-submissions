class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        biggestFrequency = 0
        for key, value in freqMap.items():
            if value > biggestFrequency:
                biggestFrequency = value
        freqList = [[] for _ in range(biggestFrequency)]
        for key, value in freqMap.items():
            freqList[value - 1].append(key)
        resultList = []
        counter = 0
        for i in range(len(freqList) - 1, -1, -1):
            while freqList[i]:
                if counter == k:
                    return resultList
                resultList.append(freqList[i].pop())
                counter += 1
        return resultList