import random
matrix = [[0]*5 for i in range(5)]
for i in range(5):
	for j in range(5):
		matrix[i][j] = random.randint(1,100)
Nmatrix = []
col = [set(),set(),set(),set(),set()]
n=0
N=3
for n in range(N):
	for j in range(5):
		for i in range(5):
			matrix[i][j] = random.randint(1,100)
		col_code = ""
		for ii in range(5):
			col_code+=str(matrix[ii][j])
		if col_code in col[j]:
			j-=1
		else:
			col[j].add(col_code)
	Nmatrix.append(matrix)
print(Nmatrix)