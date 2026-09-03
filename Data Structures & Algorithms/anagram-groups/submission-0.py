class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(ord("a")) # 97
        anMap = {}
        for word in strs:
            destructeredWord = [[] for _ in range(26)]
            for c in word:
                destructeredWord[ord(c) - 97].append(c)
            wordCountAsTuple = tuple([len(characterList) for characterList in destructeredWord])
            if wordCountAsTuple in anMap:
                anMap[wordCountAsTuple].append(word)
            else:
                anMap[wordCountAsTuple] = []
                anMap[wordCountAsTuple].append(word)
        return [value for key,value in anMap.items()]