class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    # windowStart, res, currSum = 0, 1e8, 0
    # move windowEnd from (0, len(arr)):
    #   add arr[windowEnd] to currSum
    #   if currSum >= s:
    #     res = min(res, windowEnd - windowStart)
    #     windowStart += 1
    # return res
        windowStart, res, currSum = 0, 1e8, 0

        for windowEnd in range(0, len(nums)):
            currSum += nums[windowEnd]

            if currSum >= target:
                while currSum >= target:
                    res = min(res, windowEnd - windowStart + 1)
                    currSum -= nums[windowStart]
                    windowStart += 1
        
        if res == 1e8: return 0

        return res