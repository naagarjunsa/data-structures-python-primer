from binarytree import BinaryTree, TreeNode

def get_binary_tree_size(node):
    if node is None:
        return 0
    
    return 1 + get_binary_tree_size(node.left) + get_binary_tree_size(node.right)


if __name__ == "__main__":
    
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    

    print(get_binary_tree_size(tree.root))