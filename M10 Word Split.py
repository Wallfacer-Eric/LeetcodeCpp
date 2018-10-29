s = "aaaa bbb cccc ddd ee ff ggggg"
s = s.split(' ')
k=10
remain = k
cur = ""
ans = []
for word in s:
	if len(word)>=k:
		ans.append(cur)
		cur=""
		remain = k
		ans.append(word)
		continue
	if len(word)+1>remain:
		ans.append(cur)
		cur=""
		remain = k
	if cur:
		cur+=' '
	cur+=word
	remain = k-len(cur)
if cur:
	ans.append(cur)
print(ans)