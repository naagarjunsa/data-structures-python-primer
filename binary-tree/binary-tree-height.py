from binarytree import BinaryTree, TreeNode


def get_height(node):
    if node is None:
        return -1
    
    return 1 + max(get_height(node.left), get_height(node.right))


if __name__ == "__main__":
    
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    

    print(get_height(tree.root))

