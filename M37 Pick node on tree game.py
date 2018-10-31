def countnode(root):
	if not root:
		return 0
	return 1+countnode(root.left)+countnode(root.right)
l = countnode(start.left)
r = countnode(start.right)
f = countnode(root)-countnode(start)
if max(l,r,f)==0: print("have no choice")
if l==max(l,r,f): print("left child of start node")
if r==max(l,r,f): print("right child of start node")
if f==max(l,r,f): print("father of start node")