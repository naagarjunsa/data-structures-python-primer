from binarytree import BinaryTree, TreeNode

def levelorder(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)

    while queue != []:
        temp = queue.pop(0)
        print(temp.val, end="-> ")
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

if __name__ == "__main__":
    
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    
    levelorder(tree.root)
    print("None")
