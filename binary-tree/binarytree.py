class TreeNode:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BinaryTree:

    def __init__(self, val):
        self.root = TreeNode(val)
    
    def inorder(self, TreeNode):
        if TreeNode is None:
            return
        
        self.inorder(TreeNode.left)
        print(TreeNode.val, end="-> ")
        self.inorder(TreeNode.right)

    
if __name__ == "__main__":
    
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    
    tree.inorder(tree.root)


    
