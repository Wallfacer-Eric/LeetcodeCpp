word = "hellloooo"
i = 0
j = 0
ans = []
while j!=len(word):
	print(i,j,word[i],word[j])
	if word[j] == word[i]:
		j+=1
	else:
		if j-i>=3:
			ans.append([i,j-1])
		i=j
if j-i>=3:
	ans.append([i,j-1])
print(ans)