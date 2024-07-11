# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # sorted array from inorder traversal
        # self.res = []
        # def helper(node):
        #     if node.left and helper(node.left): return True

        #     self.res.append(node)
        #     if len(self.res) > 2:
        #         if self.res[-1].val < self.res[-2].val and self.res[-2].val < self.res[-3].val: 
        #             self.res[-1].val, self.res[-3].val = self.res[-3].val, self.res[-1].val
        #             return True
        #         elif self.res[-2].val < self.res[-3].val: 
        #             self.res[-3].val, self.res[-2].val = self.res[-2].val, self.res[-3].val
        #             return True
        #         elif self.res[-1].val < self.res[-2].val: 
        #             self.res[-1].val, self.res[-2].val = self.res[-2].val, self.res[-1].val
        #             return True
            
        #     if node.right and helper(node.right): return True

        #     return False

        # if not helper(root) and len(self.res) == 2 and self.res[-1].val < self.res[-2].val: self.res[-1].val, self.res[-2].val = self.res[-2].val, self.res[-1].val

        # recursive inorder traversal
        # self.first = None
        # self.second = None
        # self.prev = None
        # def helper(node):
        #     if node.left: helper(node.left)

        #     if self.prev != None and node.val < self.prev.val:
        #         if self.first == None: self.first = self.prev
        #         self.second = node
            
        #     self.prev = node

        #     if node.right: helper(node.right)

        # helper(root)
        # self.first.val, self.second.val = self.second.val, self.first.val

        # iterative inorder traversal
        # first = None
        # second = None
        # prev = None
        # stk = []
        # while stk or root:
        #     while root:
        #         stk.append(root)
        #         root = root.left
        #     root = stk.pop()

        #     if prev and root.val < prev.val:
        #         second = root
        #         if first == None: first = prev
        #         else: break
        #     prev = root
        #     root = root.right

        # first.val, second.val = second.val, first.val

        # inorder morris traversal
        first = second = prev = None
        pred, curr = None, root

        while curr:
            if curr.left == None:
                if prev and curr.val < prev.val:
                    second = curr
                    if first == None: first = prev
                prev = curr
                
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr: pred = pred.right

                if pred.right == None:
                    pred.right = curr
                    curr = curr.left
                else:
                    if prev and curr.val < prev.val:
                        second = curr
                        if first == None: first = prev
                    prev = curr

                    pred.right = None
                    curr = curr.right
        
        first.val, second.val = second.val, first.val