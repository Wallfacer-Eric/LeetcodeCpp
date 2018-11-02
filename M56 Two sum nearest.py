s = [1,2,3,4,5,6,7,8,2,3,5,2,5,2,5,7,1]
target = 10.1
s.sort()
i = 0
j = len(s)-1
while i<j:
	if s[i]+s[j]>target:
		try:
			upbound = min(upbound,s[i]+s[j])
		except:
			upbound = s[i]+s[j]
		j-=1
	elif s[i]+s[j]<target:
		try:
			lobound = max(lobound,s[i]+s[j]) 
		except:
			lobound = s[i]+s[j]
		i+=1
	else:
		print(target)
if upbound-target<target-lobound:
	print(upbound)
else:
	print(lobound)