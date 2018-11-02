intervals = [[1,2],[3,8],[4,7],[6,10]]
intervals.sort(key=lambda x:x[1])
overlap = [1 for i in intervals]
for i in range(1,len(intervals)):
	for j in range(i-1,-1,-1):
		if intervals[j][1]>intervals[i][0]:
			overlap[j]+=1
		else:
			break
print(overlap)