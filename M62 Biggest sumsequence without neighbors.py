s = [1,2,3,4,5,6,7,8,2,3,5,2,5,2,5,7,1]
dp = [0 for i in range(len(s))]
if len(s)<3:
	print(max(s))
dp[0]=s[0]
dp[1]=max(s[0],s[1])
for i in range(2,len(dp)):
	dp[i] = max(dp[i-2]+s[i],dp[i-1])
print (dp[-1])