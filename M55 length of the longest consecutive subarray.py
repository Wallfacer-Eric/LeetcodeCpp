s = [1,3,5,7,8,9]
i = 0
j = 0
res = 0
while j<len(s):
	if i==j:
		j+=1
		continue
	if s[j]==s[j-1]+1:
		j+=1
	else:
		res = max(res, j-i)
		i=j
res = max(res,j-i)
print(res)