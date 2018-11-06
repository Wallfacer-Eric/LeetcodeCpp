class treenode:
	def __init__(self):
		self.val=0
		self.left=None
		self.right=None
		self.parent=None
		self.sibling=None
def linkSibling(root):
	queue = [root]
	while len(queue)>0:
		for i in range(len(queue)-1):
			queue[i].sibling=queue[i+1]
		temp = queue
		queue = []
		for i in temp:
			if i.left:  queue.append(i.left)
			if i.right: queue.append(i.right)