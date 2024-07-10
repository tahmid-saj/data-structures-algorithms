class LargerNumKey(str):
    def __lt__(a, b):
        return a + b > b + a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # turn nums[i] into strings
        # sort the strings then join
        listStr = map(str, nums)
        nums = list(listStr)
        nums.sort(key=LargerNumKey)

        if nums[0] == "0": return "0"

        return "".join(nums)