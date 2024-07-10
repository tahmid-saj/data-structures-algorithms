class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # quadratic time, linear time
        # return self.quadraticTime(nums)
        return self.linearTime(nums)
    
    def quadraticTime(self, nums):
        res = -math.inf

        for i in range(len(nums)):
            curr = 1
            for j in range(i, len(nums)):
                curr *= nums[j]
                res = max(res, curr)
        
        return res
    
    def linearTime(self, nums):
        localMax, localMin, res = 1, 1, -math.inf

        for i in range(len(nums)):
            tmpMax = max(localMax * nums[i], localMin * nums[i], nums[i])
            localMin = min(localMin * nums[i], localMax * nums[i], nums[i])
            localMax = tmpMax
            res = max(res, localMax)
        
        return res