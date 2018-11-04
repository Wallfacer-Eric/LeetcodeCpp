s = "abcdefghijklmnopqrstuvwxyz"
t = "jqy"
i=0
j=0
while j<len(t):
	while i<len(s):
		if s[i]==t[j]:
			i+=1
			j+=1
			break
		i+=1
	if i>=len(s):
		break
if j==len(t):
	print(True)
else:
	print(False)