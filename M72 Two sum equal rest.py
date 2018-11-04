s = [4,1,5]
total = sum(s)
s.sort()
i=0
j=len(s)-1
while i<j:
	if s[i]+s[j]<total-s[i]-s[j]:
		i+=1
	elif s[i]+s[j]>total-s[i]-s[j]:
		j-=1
	else:
		print(s[i],s[j])
		break
if i==j:
	print("No result")