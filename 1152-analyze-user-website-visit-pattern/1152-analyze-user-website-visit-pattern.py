class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_history = {}
        #seperates out the users into multiple list
        for i in range(len(username)):
            if username[i] in user_history:
                user_history[username[i]].append((timestamp[i], website[i]))
            else:
                user_history[username[i]] = [(timestamp[i], website[i])]

        pattern_track = {}
        #goes through the user
        for user in user_history:

            #sort the user's history with timestamp
            user_history[user].sort()

            #gets all unique combinations of their history and unzips the timestamp
            all_triplets = set(combinations([y for x, y in user_history[user]], 3))

            #goes through all the triplets 
            for route in all_triplets:
                #and adds the amount of times they've been visited
                if route in pattern_track:
                    pattern_track[route] += 1
                else:
                    pattern_track[route] = 1

        longest = 0
        ans = None

        #goes through a sorted version of the triplets, and gets the most visited
        for pattern in sorted(pattern_track.keys()):
            if pattern_track[pattern] > longest:
                longest = pattern_track[pattern]
                ans = pattern
                
        return ans
#         userDict = {}
#         for i in range(len(username)):
#             if username[i] in userDict:
#                 userDict[username[i]].append((timestamp[i], website[i]))
#             else:
#                 userDict[username[i]] = [(timestamp[i], website[i])]
        
#         patternScore = {}
#         for user in userDict:
#             userDict[user].sort()
            
#             patterns = set(combinations([website for timestamp, website in userDict[user]], 3))
            
#             for pattern in patterns:
#                 if pattern in patternScore:
#                     patternScore[(pattern)] += 1
#                 else:
#                     patternScore[pattern] = 1
#         maxScore = 0
#         result = None
        
#         for pattern in patternScore:
#             if patternScore[pattern] > maxScore:
#                 result = pattern
#                 maxScore = patternScore[pattern]
                
#         return list(result)
        
