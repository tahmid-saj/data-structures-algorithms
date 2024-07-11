class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)
        # self.end = False
        # return self.recursive(nums, len(nums) - 1)
    
        return self.dp(nums)

    def recursive(self, nums, index):
        path1 = nums[index]
        if index - 2 >= 0:
            if index == len(nums) - 1: self.end = True
            path1 += self.recursive(nums, index - 2)
        path2 = 0
        if index - 1 >= 0:
            if index == len(nums) - 1: self.end = False
            path2 = self.recursive(nums, index - 1)
        
        if index <= 1:
            if self.end and index == 1: return nums[index]
            elif self.end and index == 0: return 0
        
        if index == 0: return nums[index]

        return max(path1, path2)
    
    def dp(self, nums):
        prev, curr = nums[-1], max(nums[-1], nums[-2])
        for i in range(len(nums) - 3, 0, -1):
            tmp = max(nums[i] + prev, curr)
            prev = curr
            curr = tmp
        max1 = curr

        prev, curr = nums[-2], max(nums[-2], nums[-3])
        for i in range(len(nums) - 4, -1, -1):
            tmp = max(nums[i] + prev, curr)
            prev = curr
            curr = tmp
        max2 = curr

        return max(max1, max2)