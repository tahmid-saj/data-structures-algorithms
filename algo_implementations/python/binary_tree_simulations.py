# sorted array to BST using sorted array
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
  def helper(l, r):
    if l > r: return None
    middle = l + (r - l) // 2
    node = TreeNode(nums[middle])
    node.left = helper(l, middle - 1)
    node.right = helper(middle + 1, r)
    return node

  return helper(0, len(nums) - 1)

# sorted linked list to binary search tree

# inorder and preorder arrays to binary tree
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inorderNodes = {}
    for i, v in enumerate(inorder): inorderNodes[v] = i
    preorderIndex = 0

    def helper(l, r):
      nonlocal preorderIndex
      if l > r: return None
      rootVal = preorder[preorderIndex]
      node = TreeNode(rootVal)
      preorderIndex += 1
      
      node.left = helper(l, inorderNodes[rootVal] - 1)
      node.right = helper(inorderNodes[rootVal] + 1, r)
      return node
      
    return helper(0, len(inorder) - 1)

# inorder and postorder arrays to binary tree
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
  inorder_nodes = {}
  for i, v in enumerate(inorder): inorder_nodes[v] = i
  postorder_index = len(postorder) - 1

  def helper(l, r):
    nonlocal postorder_index
    if l > r: return None

    rootVal = postorder[postorder_index]
    mid = inorder_nodes[rootVal]
    postorder_index -= 1

    right = helper(mid + 1, r)
    left = helper(l, mid - 1)

    node = TreeNode(rootVal)
    node.right = right
    node.left = left

    return node
    
  return helper(0, len(inorder) - 1)