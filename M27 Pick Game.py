maxChoosableInteger=3
desiredTotal=3
def DFS(turn,used,cur,desiredTotal):
	if cur>=desiredTotal:
		return -turn
	for i in range(1,maxChoosableInteger+1):
		if used[i]: continue
		print('a',used)
		used[i]=1
		result =DFS(-turn,used,cur+i,desiredTotal)
		used[i]=0
		print('b',used)
		if turn*result>0:
			return turn
	return -turn
used = [0 for i in range(maxChoosableInteger+1)]
if DFS(1,used,0,desiredTotal)==1:
	print(True)
else:
	print(False)