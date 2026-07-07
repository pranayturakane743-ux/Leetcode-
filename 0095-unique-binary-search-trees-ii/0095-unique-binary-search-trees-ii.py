class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def build_trees(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            # Pick a root 'i'
            for i in range(start, end + 1):
                # All left subtrees with values < i
                left_trees = build_trees(start, i - 1)
                # All right subtrees with values > i
                right_trees = build_trees(i + 1, end)
                
                # Combine left and right subtrees
                for l in left_trees:
                    for r in right_trees:
                        current_root = TreeNode(i)
                        current_root.left = l
                        current_root.right = r
                        all_trees.append(current_root)
            
            return all_trees
        
        return build_trees(1, n) if n > 0 else []