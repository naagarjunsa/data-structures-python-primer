from binarytree import BinaryTree, TreeNode

def preorder(node):
    if node is None:
        return
    
    print(node.val, end="-> ")
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    if node is None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.val, end="-> ")

def inorder( node):
    if node is None:
        return
    
    inorder(node.left)
    print(node.val, end="-> ")
    inorder(node.right)

if __name__ == "__main__":
    
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    

    preorder(tree.root)
    print("None")
    postorder(tree.root)
    print("None")
    inorder(tree.root)
    print("None")