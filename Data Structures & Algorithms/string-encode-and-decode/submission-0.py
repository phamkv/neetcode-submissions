class Solution:

    def encode(self, strs: List[str]) -> str:
        # #5#Hello#5#
        encodedString = ""
        for string in strs:
            prefix = "#" + str(len(string)) + "#"
            encodedString += prefix + string
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStringList = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                length = ""
                i += 1
                while s[i] != "#":
                    length += s[i]
                    i += 1
                nextIndex = i + 1 + int(length)
                decodedStringList.append(s[i + 1:nextIndex])
                i = nextIndex
        return decodedStringList