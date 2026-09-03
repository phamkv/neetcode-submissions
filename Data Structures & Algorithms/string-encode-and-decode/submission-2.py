class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for word in strs:
            encodedString += str(len(word)) + "#" + word
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1+length
            decodedStrs.append(s[j+1:i])
        return decodedStrs