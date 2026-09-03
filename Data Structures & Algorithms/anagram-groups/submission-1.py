class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            freq = [0 for _ in range(26)]
            for c in word:
                freq[ord(c) - ord("a")] += 1
            freqTuple = tuple(freq)
            if freqTuple not in group:
                group[freqTuple] = []
            group[freqTuple].append(word)
        return [v for k,v in group.items()]