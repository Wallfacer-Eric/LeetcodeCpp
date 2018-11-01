def rightmost(root):
	while root.right:
		root=root.right
	return root
def treesum(root):
	treesum = 0
	while root:
		if root.left:
			rightmost(root.left).right = root
			temp = root.left
			root.left=NULL
			root = temp
		else:
			treesum+=root.val
			root=root.right
	return treesum