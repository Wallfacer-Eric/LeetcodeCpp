import random
N = 100
s=0
for j in range(10000):
	M = [1 for i in range(N)]
	for i in range(198):
		ran = random.randint(0,len(M)-1)
		if M[ran]==0.5:
			M.pop(ran)
		elif M[ran]==1:
			M.pop(ran)
			M.append(0.5)
	if len(M)==1:
		s+=1
print(s/10000)