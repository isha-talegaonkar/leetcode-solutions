class Solution:
    def minimumPushes(self, word: str) -> int:
        hashmap = defaultdict(int)
        
        for char in word:
            hashmap[char] += 1
        
        frequencies = [-freq for freq in hashmap.values()]
        heapq.heapify(frequencies)
        # print(frequencies)
        
        result = 0
        index = 0
        while frequencies:
            # freq = frequencies[0]
            result += (1+(index//8)) * (-heapq.heappop(frequencies))
            # print(index, index//8, result, freq)
            index += 1
        
        return result
        
        