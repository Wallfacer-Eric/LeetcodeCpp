tree = [[0,100],[0,200],[1,400],[0,300],[3,500],[3,600]]
delete_id = 1
tree[delete_id][0]=-1
for i in range(delete_id+1,len(tree)):
	print(tree[tree[i][0]][0])
	if tree[tree[i][0]][0]==-1:
		tree[i][0]=-1
minus = []
m=0
i=0
while i<len(tree):
	if tree[i][0]==-1:
		m+=1
		minus.append(-1)
		tree.pop(i)
	else:
		minus.append(m)
		tree[i][0]-=minus[tree[i][0]]
		i+=1
print(minus,tree)