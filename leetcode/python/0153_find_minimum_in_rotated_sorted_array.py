class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            middle = l + (r - l) // 2

            if middle > 0 and nums[middle - 1] > nums[middle]: return nums[middle]
            elif middle < len(nums) - 1 and nums[middle] > nums[middle + 1]: return nums[middle + 1]

            if nums[l] <= nums[middle] and nums[middle] > nums[r]: l = middle + 1
            else: r = middle
        
        return nums[l]