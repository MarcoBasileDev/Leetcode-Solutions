class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, root, None)
        
        def dfs(root, lvl):
            if not root:
                return
            
            lvl -= 1

            if lvl == 1:
                root.left = TreeNode(val, root.left, None)
                root.right = TreeNode(val, None, root.right)
            else:
                dfs(root.left, lvl)
                dfs(root.right, lvl)
            
        dfs(root, depth)

        return root

        # Time Complexity O(n)
        # Space Complexity O(1)