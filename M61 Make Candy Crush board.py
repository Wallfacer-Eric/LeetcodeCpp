import random
N=8
M=8
color = 3
board = [[-1]*N for i in range(M)]
for i in range(M):
	for j in range(N):
		valid = {1,2,3}
		if i>1 and board[i-2][j]==board[i-1][j]:
			if board[i-1][j] in valid:   valid.remove(board[i-1][j])
		#if i<M-2 and board[i+2][j]==board[i+1][j]:
		#	if board[i+1][j] in valid: valid.remove(board[i+1][j])
		#if i>0 and i<M-1 and board[i-1][j]==board[i+1][j]:
		#	if board[i+1][j] in valid: valid.remove(board[i+1][j])
		if j>1 and board[i][j-2]==board[i][j-1]:
			if board[i][j-1] in valid: valid.remove(board[i][j-1])
		#if j<N-2 and board[i][j+2]==board[i][j+1]:
		#	if board[i][j+1] in valid: valid.remove(board[i][j+1])
		#if j>0 and j<N-1 and board[i][j-1]==board[i][j+1]:
		#	if board[i][j+1] in valid: valid.remove(board[i][j+1])
		valid = list(valid)
		board[i][j] = valid[random.randint(0,len(valid)-1)]
print (board)