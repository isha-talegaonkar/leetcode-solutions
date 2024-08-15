class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(numbers)):
            complement = target - numbers[i]
            
            if complement in hashmap:
                return [hashmap[complement]+1, i+1]
            hashmap[numbers[i]] = i
                
                