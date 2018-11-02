def findnear(root, target):
	up = 99999999
	down = -99999999
	while root:
		if root.val>target:
			up = min(up,root.val)
			root = root.left
		elif root.val<target:
			down = max(down,root.val)
			root = root.right
		else:
			return target
	if up-target>target-down:
		return down
	else:
		return up