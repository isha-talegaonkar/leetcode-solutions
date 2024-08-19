class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        userDict = {}
        for i in range(len(username)):
            if username[i] in userDict:
                userDict[username[i]].append([timestamp[i], website[i]])
            else:
                userDict[username[i]] = [[timestamp[i], website[i]]]
        
        print(userDict)
        patternScore = {}
        for user in userDict:
            userDict[user].sort(key=lambda x: x[0])
            
            patterns = set(combinations([website for timestamp, website in userDict[user]], 3))
            
            for pattern in patterns:
                if pattern in patternScore:
                    patternScore[(pattern)] += 1
                else:
                    patternScore[pattern] = 1
        maxScore = 0
        result = None
        
        for pattern in sorted(patternScore.keys()):
            if patternScore[pattern] > maxScore:
                result = pattern
                maxScore = patternScore[pattern]
                
        return result
        
