class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._left_inorder(root)

    def _left_inorder(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        nested_node = self.stack.pop()
        
        if nested_node.right:
            self._left_inorder(nested_node.right)
            
        return nested_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0