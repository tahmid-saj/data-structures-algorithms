class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1: 4 1 2
        # nums2: 1 3 4 2
        # map:   3 4 -1 -1
        if len(nums2) == 0: return []

        stack, mapping, res = [], {}, []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        
        for i in range(0, len(stack)):
            mapping[stack[i]] = -1

        for i in range(0, len(nums1)):
            res.append(mapping[nums1[i]])

        return res