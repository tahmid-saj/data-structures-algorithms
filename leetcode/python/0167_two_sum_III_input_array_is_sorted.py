class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r, res = 0, len(numbers) - 1, [-1, -1]

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target: return [l + 1, r + 1]
            elif s < target: l += 1
            elif s > target: r -= 1

        return res