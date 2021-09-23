class BinaryTreeNode:
    """
    Node class of binary tree with root, left child and right child
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#------------------------------------------Function 1------------------------------------------------------
def printTree(root):
    """
    printing tree in a normal way.
    Note: Tree traversal we will use in further files.

    Args:
        root ([Binary Tree root Node]): Taking binary tree root and printing entire tree.
    """
    if root == None:
        return
    print(root.data, end=": ")
    if root.left != None:
        print("L", root.left.data, end=', ')
    if root.right != None:
        print("R", root.right.data, end=" ")
    print()
    printTree(root.left)
    printTree(root.right)
    
#------------------------------------------Function 2------------------------------------------------------
def treeInput():
    """
    Taking input in binary tree from user.
    Note: This is not an intuitive way. we will implement that too.  

    Returns:
        returning root of the tree.
    """
    rootData = int(input("Enter data: "))
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

#------------------------------------------Function 3------------------------------------------------------
def countTreeNodes(root):
    if root == None:
        return 0
    leftNodes = countTreeNodes(root.left)
    rightNodes = countTreeNodes(root.right)
    return  1 + leftNodes + rightNodes

#Creating objects of Binary tree node manually
# btn1 = BinaryTreeNode(1)
# btn2 = BinaryTreeNode(2)
# btn3 = BinaryTreeNode(3)

#Making connection of left and right childs and all.
# btn1.left = btn2
# btn1.right = btn3

# root = treeInput()
# printTree(root)
# print(countTreeNodes(root))