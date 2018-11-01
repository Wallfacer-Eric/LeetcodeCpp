import heapq
import bisect
n = 20
chair = [3,5,9,16]
people = 10
pq = []
ans = []
for i in range(people):
	if not chair:
		ans.append(n//2)
		bisect.insort(chair,n//2)
		continue
	start = chair[0]-0
	end = n-chair[-1]
	if start>=end:
		pos = 0
	else:
		pos = n
	lenth = max(start,end)
	for j in range(len(chair)-1):
		if -(-(chair[j+1]-chair[j]-1)//2) > lenth:
			lenth = -(-(chair[j+1]-chair[j]-1)//2)
			pos = (chair[j+1]+chair[j])//2
	ans.append(pos)
	bisect.insort(chair,pos)
print(ans)