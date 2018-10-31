import bisect
a=[2,3,6,8,5,7,43,3,5,3,6,6,7]
b=[3,3,4,323,66,78,4,212,4,5]
k = 10
ans = []
for i in a:
	for j in b:
		bisect.insort(ans,i+j)
		if len(ans)==k:
			ans.pop(0)
print(ans)