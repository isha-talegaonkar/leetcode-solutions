class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = defaultdict(int)
        res = []
        for char in s:
            hashmap[char] += 1
            
        priorityQ = [(-count, char) for char, count in hashmap.items()]
        heapify(priorityQ)
        
        while priorityQ:
            count1, char1 = heappop(priorityQ)
            if not res or char1 != res[-1]:
                res.append(char1)
                if (count1 + 1) != 0:
                    heappush(priorityQ, (count1+1, char1))
            else:
                if not priorityQ: return ''
                count2, char2 = heappop(priorityQ)
                res.append(char2)
                if (count2 + 1) != 0:
                    heappush(priorityQ, (count2+1, char2))
                heappush(priorityQ, (count1, char1))
            print(priorityQ)
        
        print("outside PQ")
        return ''.join(res)
                    
            
            
            
        
        
        
        