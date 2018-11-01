s = [3,5,7,4,3,5,7,5,7,7,4,7,1,0,8,9]
new = []
for i in range(len(s)-1):
	for j in range(i+1, len(s)):
		if s[j]>s[i]:
			new.append(j)
			break
	if j==len(s):
		new.append(-1)
new.append(-1)
print(new)