class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return self.monotonicStack(nums)
    
    def monotonicStack(self, nums):
        stk = []
        secondMax = -math.inf

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < secondMax: return True
            while stk and stk[-1] < nums[i]:
                secondMax = stk.pop()
            stk.append(nums[i])
        
        return False