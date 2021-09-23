class BinaryTreeNode:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data


# A function to do inorder tree traversal
def inorder(root):

	if root:

		# First recur on left child
		inorder(root.left)

		# then print the data of BinaryTreeNode
		print(root.data, end= " ")

		# now recur on right child
		inorder(root.right)


# A function to do postorder tree traversal
def postorder(root):

	if root:

		# First recur on left child
		postorder(root.left)

		# the recur on right child
		postorder(root.right)

		# now print the data of BinaryTreeNode
		print(root.data, end=" "),


# A function to do preorder tree traversal
def preorder(root):

	if root:

		# First print the data of BinaryTreeNode
		print(root.data, end=" "),

		# Then recur on left child
		preorder(root.left)

		# Finally recur on right child
		preorder(root.right)


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
print ("Preorder traversal of binary tree is")
preorder(root)

print ("\nInorder traversal of binary tree is")
inorder(root)

print ("\nPostorder traversal of binary tree is")
postorder(root)
