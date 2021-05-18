from binarytree import BinaryTree, TreeNode

def reverselevelorder(self):
    if self.root is None:
        return
    
    stack = []
    queue = []
    queue.append(self.root)

    while queue != []:
        temp = queue.pop(0)
        stack.append(temp)
        if temp.right:
            queue.append(temp.right)
        if temp.left:
            queue.append(temp.left)
    
    while stack != []:
        print(stack.pop().val, end="-> ")

if __name__ == "__main__":
    
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    

    reverselevelorder(tree)
    print("None")
