class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        freqBucket = defaultdict(list)
        for key, v in freq.items():
            freqBucket[v].append(key)
        highestFreq = max(freqBucket.keys())
        i = 0
        result = []
        while True:
            while freqBucket[highestFreq]:
                result.append(freqBucket[highestFreq].pop())
                i += 1
                if i == k:
                    return result
            highestFreq -= 1
        
