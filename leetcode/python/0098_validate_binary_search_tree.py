# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.constantSpaceDPDFS(root)

        # return self.recursiveLimits(root)

        # return self.iterativeLimits(root)

        # return self.recursiveInorder(root)

        return self.iterativeInorder(root)

    def constantSpaceDPDFS(self, root):
        self.dp = []

        def helper(node):
            if node.left and helper(node.left) == False: return False

            self.dp.append(node)
            if len(self.dp) == 2 and self.dp[-2].val >= self.dp[-1].val: return False
            if len(self.dp) == 2: self.dp.pop(0)

            if node.right and helper(node.right) == False: return False

            return True

        if helper(root) == False: return False
        return True
    
    def recursiveLimits(self, root):
        def helper(node, low=-math.inf, high=math.inf):
            if node == None: return True

            if node.val <= low or node.val >= high: return False

            if helper(node.left, low, node.val) == False: return False
            if helper(node.right, node.val, high) == False: return False

        if helper(root) == False: return False
        return True
    
    def iterativeLimits(self, root):
        if root == None: return True

        stk = []
        stk.append((root, -math.inf, math.inf))

        while stk:
            node, low, high = stk.pop()

            if node.val <= low or node.val >= high: return False
            if node.left: stk.append((node.left, low, node.val))
            if node.right: stk.append((node.right, node.val, high))

        return True
    
    def recursiveInorder(self, root):
        self.prev = -math.inf
        def helper(node):
            if node.left and helper(node.left) == False: return False

            if node.val <= self.prev: return False
            self.prev = node.val

            if node.right and helper(node.right) == False: return False

        if helper(root) == False: return False
        return True
    
    def iterativeInorder(self, root):
        stk, prev = [], -math.inf

        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()

            if root.val <= prev: return False
            prev = root.val
            root = root.right
        
        return True