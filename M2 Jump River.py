river = "o-oo-o-o--"
if len(river)<2:
	print(True)
dp = [0 for i in river]
if river[0]=='o':
	dp[0]=1
if river[1]=='o':
	dp[1]=1
for i in range(2,len(river)):
	if river[i]=='o':
		dp[i] = max(dp[i-2],dp[i-1])
print(dp)
print(max(dp[-1],dp[-2]))