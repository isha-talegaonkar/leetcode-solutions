class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordLen = len(word)
        abbrLen = len(abbr)
        
        wordPointer, abbrPointer = 0, 0
        
        while wordPointer < wordLen and abbrPointer < abbrLen:
            if abbr[abbrPointer].isdigit():
                if abbr[abbrPointer] == '0':
                    return False
                skip = 0
                while abbrPointer < abbrLen and abbr[abbrPointer].isdigit():
                    skip = 10 * skip + int(abbr[abbrPointer])
                    abbrPointer += 1
                wordPointer += skip
                if wordPointer >wordLen:
                    return False
            else:
                if word[wordPointer] != abbr[abbrPointer] or wordPointer >= wordLen:
                    return False
                wordPointer += 1
                abbrPointer += 1
        return wordPointer == wordLen and abbrPointer == abbrLen
        