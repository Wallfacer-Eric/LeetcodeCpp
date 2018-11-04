s=[0.13,0.57,0.91,0.78,0.69,0.33,0.25,0.41,0.09,0.04]
ans = []
def dfs(s,formula,value):
	if not s:
		if value>0 and value<0.12:
			ans.append([formula,value])
		return
	dfs(s[1:],formula+'+'+str(s[0]),value+s[0])
	dfs(s[1:],formula+'-'+str(s[0]),value-s[0])
dfs(s[1:],str(s[0]),s[0])
for i in ans:
	print (i)