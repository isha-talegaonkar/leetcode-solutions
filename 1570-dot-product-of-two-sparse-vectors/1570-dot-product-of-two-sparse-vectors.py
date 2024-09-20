class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = defaultdict(int)
        
        for i, num in enumerate(nums):
            if num != 0:
                self.vector[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, num in self.vector.items():
            if i in vec.vector:
                result += num * vec.vector[i]
        
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)